from django.db import models


class Services(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.name

class Reviews(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    review = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name