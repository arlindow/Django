from django.shortcuts import render, redirect
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


def novo_funcionario(request):

    
    if request.method == "POST":
        #print("POST RECEBIDO")
        #print(request.POST)

        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        cpf = request.POST.get("cpf")
        tempo_de_servico = request.POST.get("tempo_de_servico")
        remuneracao = request.POST.get("remuneracao")

        Funcionario.objetos.create(
            nome = nome,
            sobrenome = sobrenome,
            cpf = cpf,
            tempo_de_servico = tempo_de_servico,
            remuneracao = remuneracao
        )

        return redirect('website:lista_funcionarios')

    return render(request, 'novo_funcionario.html')