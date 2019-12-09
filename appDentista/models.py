from django.db import models

# Create your models here.
class Dentista(models.Model):
    name=models.CharField(max_length=100, blank=False)
    cpf=models.CharField(max_length=11, blank=False, primary_key=True)
    cro=models.CharField(max_length=7, blank=False)
    email=models.EmailField(max_length=50, blank=False)
    password=models.CharField(max_length=50, blank=False)
    passwordConfirmation=models.CharField(max_length=30, blank=False)
    street=models.CharField(max_length=100, blank=False)
    number=models.IntegerField(blank=False)
    district=models.CharField(max_length=50, blank=False)
    city=models.CharField(max_length=50, blank=False)
    state=models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class Produtos(models.Model):
    name=models.CharField(max_length=100, blank=False)
    lab=models.CharField(max_length=50, blank=False)
    value=models.DecimalField(max_digits=6, decimal_places=2, blank=False)

    def __str__(self):
        return self.name
