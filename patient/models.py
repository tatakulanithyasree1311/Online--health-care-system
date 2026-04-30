from django.db import models

class Patient(models.Model):
    pid = models.IntegerField()
    pname = models.CharField(max_length=50)
    paddress = models.CharField(max_length=100)
    pphone = models.CharField(max_length=15)
    pdisease = models.CharField(max_length=50)
    pemail = models.EmailField()
    doc_designation = models.CharField(max_length=100)
    presult = models.CharField(max_length=50)
class Doctor(models.Model):
    did = models.IntegerField()
    dname = models.CharField(max_length=40)
    dqualification = models.CharField(max_length=40)
    dspecilization = models.CharField(max_length=40)
    ddesignation = models.CharField(max_length=40)
    dexperience = models.IntegerField()
    sal = models.IntegerField()
    
     