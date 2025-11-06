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

Como não temos mais o arquivo de modelos na pasta /website,
podemos, então, excluir a pasta /migrations e o migrations.py, pois
estes serão gerados e gerenciados pelo app helloworld.

