from django.db import models
from django import forms
# Create your models here.

# Appointment through doctors information 
class List (models.Model):
    Departments = models.CharField(max_length=100)
    Doctors = models.CharField(max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=12)
    message = models.TextField()

#Department model
    
class Department(models.Model):
    department_name=models.CharField(max_length=150)
    department_description=models.TextField()
    image = models.ImageField(upload_to='department_images/')
    

    def __str__(self):
        return self.department_name
#Doctors model
class DoctorDetail(models.Model):
    department_name = models.ForeignKey(Department,on_delete=models.CASCADE)
    doctor_full_name=models.CharField(max_length=150)
    gender=models.CharField(max_length=10)
    age=models.SmallIntegerField()
    education_status=models.CharField(max_length=150)
    work_experience=models.SmallIntegerField()
    email_id=models.CharField(max_length=100)
    mobile_number=models.BigIntegerField()
    doctor_description=models.TextField()
    avialiable_work_hours=models.SmallIntegerField()
    state=models.CharField(max_length=100) 
    city=models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctor_images/')
    
    
    def __str__(self):
        return self.doctor_full_name
# dynamic image according to department

#   image = models.ImageField(upload_to='department_images/', null=True, blank=True)

#Contact model

class Contact(models.Model):
    Full_name=models.CharField(max_length=150)
    Email_id=models.CharField(max_length=100)
    Query=models.CharField(max_length=100)
    Ph_number=models.BigIntegerField()
    Message=models.TextField()

    def __str__(self):
        return self.Full_name


       

