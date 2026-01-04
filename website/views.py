from django.shortcuts import render
from helloworld.models import Funcionario 

# Create your views here.
def lista_funcionarios(request):
    funcionarios = Funcionario.objetos.all()

    contexto = {
        'funcionarios': funcionarios
    }

    return render(
        request,
        "funcionarios.html",
        contexto
    )

def index(request):
    return render(request, 'funcionarios.html')