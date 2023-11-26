from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name} "


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    catergory = models.CharField(max_length=100, null=True)
    url = models.URLField()

    def __str__(self):
        return f"{self.name} - {self.url}"

class About(models.Model):
    name = models.CharField(max_length=100, null=True)
    about_me = models.CharField(max_length=500)
    image = models.ImageField(upload_to='about_us/')

    def __str__(self):
        return f"{self.name}"