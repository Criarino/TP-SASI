from django.shortcuts import render
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads

from home.models import Empresa

# Create your views here. instalar ssl em uma aplicação específica ao invés de todas , multiplos domínios para django com e s/ ssl, virtualhost apache e django

def index(request):
	return render(request,'index.html')
	
def adicionar(request):
	return render(request,'add.html')
	
@csrf_exempt
def add(request):
	if request.method == "POST":
		cnpj = request.POST['cnpj']
		solucao = request.POST['solucao']
		contato = request.POST['contato']
		data = Empresa(cnpj=cnpj, contato=contato, escolha=solucao)
		data.save()
	return render(request, 'add.html')
