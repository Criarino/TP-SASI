from django.urls import path

from . import views

urlpatterns = [
	path('', views.index),
	path('add.html', views.adicionar),
	path('index.html', views.index),
	path('lista.html', views.lista),
	path('add/', views.add, name='add'),
	path('register', views.register, name='register'),
	path('login', views.login_request, name="login"),
	path('logout', views.logout_request, name= "logout")
]
