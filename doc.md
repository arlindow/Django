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

