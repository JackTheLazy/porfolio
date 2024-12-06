from django.db import models

# Create your models here.



class Whatiknow(models.Model):
    info = models.CharField(max_length=100)

    

class Contact(models.Model):
    Contact = models.CharField(max_length=100)

class Address(models.Model):
    address = models.CharField(max_length=100)
    
class Email(models.Model):
    email = models.CharField(max_length=100)

class Education(models.Model):
    education = models.CharField(max_length=100)