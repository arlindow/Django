# python --version

Python 3.13.9

# pip --version

pip 25.2 

# python -m venv venv

# venv\Scripts\activate

erro: execução de scripts foi desabilitada neste sistema.

  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  venv\Scripts\activate

# pip install django 

listar comandos disponívies

# django-admin

Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

# django-admin startproject helloworld . (o ponto final evita criação de subpasta extra)

/helloworld
 - init
 - asgi
 - settings
 - urls
 - wsgi 
- manage

Testando

# python manage.py runserver

acesse o browser no endereço:  http://127.0.0.1:8000/

-----------------------------------------------------------------------------
#############################################################################
-----------------------------------------------------------------------------
# criar um app chamado website

Na raíz do projeto, execute:

django-admin startapp website

# crie a pasta templates dentro de website. 
Dentro dela, crie uma pasta website e dentro dela, uma pasta chamada
_layouts.

website/templates/website/layouts

# Crie também a pasta static dentro de website, para guardar os
arquivos estáticos (arquivos CSS, Javascript, imagens, fontes, etc).

Dentro dela crie uma pasta website, por questões de namespace. Dentro dela,
crie: uma pasta css, uma pasta img e uma pasta js.

website/static/website 
               css
               img
               js

Para que o Django gerencie esse app, é necessário adicioná-lo
a lista de apps instalados. Fazemos isso atualizando a configuração
INSTALLED_APPS no arquivo de configuração helloworld/settings.py

INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'helloworld',
'website'
]

vamos passar o arquivo de modelos models.py de
/website para /helloworld, pois os arquivos comuns ao projeto vão
ficar centralizados no app helloworld (geralmente temos apenas um
arquivo models.py para o projeto todo).

Como não temos mais o arquivo de modelos na pasta /website,
podemos, então, excluir a pasta /migrations e o migrations.py, pois
estes serão gerados e gerenciados pelo app helloworld.


A Camada de Modelos tem uma função essencial na arquitetura das
aplicações desenvolvidas com o Django. É nela que descrevemos os
campos e comportamentos das entidades que irão compor nosso
sistema. Também é nela que reside a lógica de acesso aos dados da nossa
aplicação. Vamos ver como é simples manipular os dados do nosso
sistema através da poderosa API de Acesso a Dados do Django.

Criando a classe Funcionario
helloworld/models.py.

Migração é a forma do Django de propagar as alterações feitas
em seu modelo (adição de um novo campo, deleção de um modelo,
etc...) ao seu esquema do banco de dados. Elas foram desenvolvidas
para serem (a maioria das vezes) automáticas, mas cabe a você
saber a hora de fazê-las, de executá-las e de resolver os problemas
comuns que você possa vir a ser submetidos.

Portanto, toda vez que você alterar o seu modelo, não se esqueça
de executar: 
python manage.py makemigrations helloworld

apenas 

python manage.py makemigrations 

deve bastar! (veja na saída do comando makemigrations: Create model
Funcionario)

Agora só falta executar o comando migrate, propriamente dito!
Para isso, vamos para a raíz do projeto e executamos:

python manage.py migrate

API DE ACESSO A DADOS

Vamos testar a adição de um novo funcionário utilizando o shell do
Django. Para isso, digite o comando: 

python manage.py shell

adicionar um novo funcionário,

from helloworld.models import Funcionario

funcionario = Funcionario(
nome='Marcos',
sobrenome='da Silva',
cpf='015.458.895-50',
tempo_de_servico=5,
remuneracao=10500.00
)
funcionario.save()

LISTAR

Funcionario.objetos.values()

Funcionario.objetos.all()
<QuerySet [<Funcionario: Funcionario object (1)>]>

# Assim mostrará o nome e sobrenome:
class Funcionario... 

def __str__(self):
        return f"{self.nome} {self.sobrenome}"

Funcionario.objetos.all()
<QuerySet [<Funcionario: Marcos da Silva>]>

Regra de ouro: Sempre que alterar seu models.py:
python manage.py makemigrations 
python manage.py migrate

através do campo objetos podemos fazer queries
incríveis sem uma linha de SQL!

Exemplo de um query um pouco mais complexa:

Busque todos os funcionários que tenham mais de 3 anos de
serviço, que ganhem menos de R$ 5.000,00 de remuneração e
que não tenham Marcos no nome.

funcionarios = Funcionario.objetos
   .exclude(name="Marcos")
   .filter(tempo_de_servico__gt=3)
   .filter(remuneracao__lt=5000.00)
   .all()

exclude() retira linhas da pesquisa
filter() filtra a busca

para filtrar por maior que concatenamos a string
__gt (gt = greater than = maiores que)

__lt (lt = less than =
menores que) para resultados menores que o valor passado.

O método .all() ao final da query serve para retornar todas as
linhas do banco que cumpram os filtros da nossa busca

o first() que retorna apenas o primeiro registro,

last(), que
retorna o último, entre outros.

vamos ver como é simples excluir um Funcionário:

funcionario = Funcionario
.objetos
.filter(id=1)
.first()
# Agora, o deletamos!
funcionario.delete()

Podemos fazer essa alteração da seguinte forma:

# Primeiro, buscamos o funcionario desejado
funcionario = Funcionario
.objetos
.filter(id=13)
.first()
# Alteramos seu sobrenome
funcionario.sobrenome = funcionario.sobrenome + " Albuquerque"
# Salvamos as alterações
funcionario.save()



CAMADA VIEW

