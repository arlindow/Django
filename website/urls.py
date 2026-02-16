from django.urls import path
from . import views 

app_name = 'website'

urlpatterns = [
    path('lista-de-funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),
    path('novo-funcionario/', views.novo_funcionario, name='novo_funcionario'),
]
