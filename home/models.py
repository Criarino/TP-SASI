from django.db import models

# Create your models here.

class Empresa(models.Model):
	cnpj=models.CharField(max_length=14)
	contato=models.CharField(max_length=50)
	escolha=models.CharField(max_length=100)
	
class Produto(models.Model):
	nome=models.CharField(max_length=20)
	descricao=models.CharField(max_length=100)
	preco=models.FloatField()
