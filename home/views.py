from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from cryptography.fernet import Fernet

from home.models import Empresa, Produto

# Create your views here.

def index(request):
	return render(request,'index.html')

def index1(request):
	return redirect('http://localhost:8080/')
	
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
	
def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('index.html')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, 'register.html', context={"register_form":form})

@csrf_exempt
def add(request):
	key=Fernet.generate_key()
	fernet = Fernet(key)
	if request.method == "POST":
		cnpj = fernet.encrypt(request.POST['cnpj'].encode())
		solucao = fernet.encrypt(request.POST['solucao'].encode())
		contato = request.POST['contato']
		data = Empresa(cnpj=cnpj, contato=contato, escolha=solucao)
		data.save()
	return render(request, 'add.html')
	
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request ,user)
				messages.info(request, "You are now logged in as {username}.")
				return redirect("index.html")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, 'login.html', context={"login_form":form})
	
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('http://localhost:8080/')
