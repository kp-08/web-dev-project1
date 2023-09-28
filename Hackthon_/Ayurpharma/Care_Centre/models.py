from django.db import models

# Create your models here.
class MedicineData(models.Model):
    name = models.CharField(max_length=100)
    symptoms= models.CharField(max_length=300)
    ayurvedic_solutions = models.CharField(max_length=300)

class Contact(models.Model):
    person_name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    date = models.DateField()
    desc = models.TextField()