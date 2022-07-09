from django.db import models

# Create your models here.

class Empresa(models.Model):
	cnpj=models.CharField(max_length=14)
	contato=models.CharField(max_length=50)
	escolha=models.CharField(max_length=100)
