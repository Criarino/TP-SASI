from django.shortcuts import render
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads

from home.models import Empresa, Produto

# Create your views here.

def index(request):
	return render(request,'index.html')
	
def adicionar(request):
	return render(request,'add.html')
	
def lista(request):
	#b = Produto(nome='teste1', descricao='Este produto é um teste', preco=float(110.10))
	#c = Produto(nome='teste2', descricao='Este produto também é um teste', preco=float(111.10))
	#d = Produto(nome='teste3', descricao='Adivinha o que este produto é', preco=float(112.10))
	#b.save()
	#c.save()
	#d.save()
	tudo={"prod": Produto.objects.all()}
	return render(request,'lista.html', tudo)
	
@csrf_exempt
def add(request):
	if request.method == "POST":
		cnpj = request.POST['cnpj']
		solucao = request.POST['solucao']
		contato = request.POST['contato']
		data = Empresa(cnpj=cnpj, contato=contato, escolha=solucao)
		data.save()
	return render(request, 'add.html')
