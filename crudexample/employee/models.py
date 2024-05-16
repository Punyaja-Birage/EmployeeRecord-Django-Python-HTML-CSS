from django.db import models

class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=200)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=20)

# Create your models here.
