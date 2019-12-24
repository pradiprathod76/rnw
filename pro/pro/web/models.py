from django.db import models

# Create your models here.

class Faq(models.Model):

    title = models.CharField(max_length=100)
    decription = models.TextField()

    def __str__(self):
        return self.title

class About(models.Model):
     title = models.CharField(max_length=100)
     decription = models.TextField()
     img = models.ImageField(upload_to='image',null=True,blank=True)

class Count(models.Model):
    title = title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='image',null=True,blank=True)
    count = models.IntegerField()

class Team(models.Model):
    name = models.CharField(max_length=100)
    deg = models.CharField(max_length=100)
    img = models.ImageField(upload_to='image',null=True,blank=True)

class Service(models.Model):
    title = models.CharField(max_length=100)
    des = models.TextField()
    img = models.ImageField(upload_to='image',null=True,blank=True)

class Project(models.Model):
    name = models.CharField(max_length=100)
    p_type = models.CharField(max_length=100)
    img = models.ImageField(upload_to='image',null=True,blank=True)

class Contact(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    msg = models.TextField()

class Blog(models.Model):
    title = models.CharField(max_length=100)
    des = models.TextField()
    img = models.ImageField(upload_to='image',null=True,blank=True)
    date = models.DateTimeField()
    cat = models.CharField(max_length=100,default=' ')

class Review(models.Model):
    name = models.CharField(max_length=100)
    pro = models.CharField(max_length=100)
    img = models.ImageField(upload_to='image',null=True,blank=True)
    msg = models.TextField()