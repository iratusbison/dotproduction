# Generated by Django 4.0.6 on 2023-11-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('about_me', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='about_us/')),
            ],
        ),
    ]