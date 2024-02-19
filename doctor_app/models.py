from django.db import models

# Create your models here.

class Admin(models.Model):
    Email = models.EmailField(max_length=20,unique=True)
    Password = models.CharField(max_length=80,default="Password")
    Role = models.CharField(max_length=20)
    Otp = models.IntegerField(max_length=20)
    is_actiive = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=True)
    is_created = models.DateTimeField(auto_now_add=True)

class Doctor(models.Model):
    Doctor = models.ForeignKey(Admin, on_delete=models.CASCADE) 
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Age = models.IntegerField(default=123)
    Address = models.CharField(max_length=255)
    Gender = models.CharField(max_length=20)
    Department = models.CharField(max_length=20)  

class Patient (models.Model):
    Patient = models.ForeignKey(Admin, on_delete=models.CASCADE) 
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Age = models.IntegerField(default=123)
    Address = models.CharField(max_length=255)
    Gender = models.CharField(max_length=20)  

    

