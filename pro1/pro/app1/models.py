from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    # def __str__(self):
    #     return self.name



class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.email

class userregister(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    add = models.TextField()
    password = models.CharField(max_length=20)

    # def __str__(self):
    #     return self.email

class image(models.Model):
    image = models.ImageField(upload_to='catimg')

class category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='cat_img')

    def __str__(self):
        return self.name
