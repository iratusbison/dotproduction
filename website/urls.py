from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name= 'home'),
    path('services/',views.explore_services,name='explore_services'),
    path('product_list/',views.explore_products,name='explore_products'),
    path('about_us/',views.about, name='about_us'),
    path('projects/',views.experimental_projects, name='projects'),
    path('designs/', views.designs,name='designs'),
    ]

