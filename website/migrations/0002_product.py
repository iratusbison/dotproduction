# Generated by Django 4.0.6 on 2023-11-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('catergory', models.CharField(max_length=100, null=True)),
                ('url', models.URLField()),
            ],
        ),
    ]
