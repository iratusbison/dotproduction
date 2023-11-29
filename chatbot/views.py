from django.http import HttpResponseRedirect
from django.shortcuts import render
import os
import pickle
import numpy as np
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
import json
import random
import nltk


nltk_data_path = [
    '/home/dotdevelopers/nltk_data',
    '/usr/local/nltk_data',
    '/usr/local/share/nltk_data',
    '/usr/local/lib/nltk_data',
    '/usr/share/nltk_data',
    '/usr/local/share/nltk_data',
    '/usr/lib/nltk_data',
    '/usr/local/lib/nltk_data'
]

# Add the NLTK data path to nltk.data.path
nltk.data.path.extend(nltk_data_path)

# Download necessary NLTK resources if needed
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('wordnet')

# Load the preprocessed data
words = pickle.load(open('chatbot/words.pkl','rb'))
classes = pickle.load(open('chatbot/classes.pkl','rb'))
model = load_model('chatbot/chatbot_model.h5')

def clean_up_sentence(sentence):
    lemmatizer = WordNetLemmatizer()
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_response(ints, intents_json):

    if not ints:
        return "Sorry, I didn't understand that."

    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

def chatbot(request):
    data_file = open('chatbot/intents.json').read()
    intents_json = json.loads(data_file)

    # Retrieve chat history from session
    chat_history = request.session.get('chat_history', [])

    if request.method == 'POST':
        message = request.POST.get('message')
        ints = predict_class(message, model)
        response = get_response(ints, intents_json)

        # Extract context if available
        context = None
        if ints and 'context' in ints[0]:
            context = ints[0]['context']

        # Append current chat to chat history
        chat_history.append({
            'message': message,
            'response': response,
            'intent': {
                'tag': ints[0]['intent'] if ints else None,
                'patterns': [pattern for intent in intents_json['intents'] for pattern in intent.get('patterns')],
                'responses': [intent['responses'] for intent in intents_json['intents'] if intent['tag'] == (ints[0]['intent'] if ints else None)],
                'context': context
            }
        })
        request.session['chat_history'] = chat_history

        # Save conversation history as a JSON file
        with open('conversation_history.json', 'w') as file:
            json.dump(chat_history, file)

        return render(request, 'chatbot.html', {'message': message, 'response': response, 'chat_history': chat_history})
    else:
        return render(request, 'chatbot.html', {'chat_history': chat_history})



def delete_chat(request):
    # Clear chat history from session
    request.session['chat_history'] = []
    return HttpResponseRedirect('bot')