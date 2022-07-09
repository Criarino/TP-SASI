from django.urls import path

from . import views

urlpatterns = {
	path('', views.index),
	path('add.html', views.adicionar),
	path('index.html', views.index),
	path('add/', views.add, name='add')
}
