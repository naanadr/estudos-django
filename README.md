# estudos-django

----
## old_versions
[![Python Version](https://img.shields.io/badge/python-3.5.7-green.svg)](https://img.shields.io/badge/python-3.5.7-green.svg)
[![Django Version](https://img.shields.io/badge/django-1.8-yellow.svg)](https://img.shields.io/badge/django-1.8-yellow.svg)

- simplemooc: Projeto desenvolvido baseado no curso [Python 3 na Web com Django](https://www.udemy.com/python-3-na-web-com-django-basico-intermediario/)
- shorturl: Desafio proposto pela Intelivix em sua [seleção de estágio](https://github.com/lacerdamarcelo/desafio_web_intelivix_dez2016)

-----
## new_versions
[![Python Version](https://img.shields.io/badge/python-3.7.4-green.svg)](https://img.shields.io/badge/python-3.7.4-green.svg)
[![Django Version](https://img.shields.io/badge/django-2.2.4-green.svg)](https://img.shields.io/badge/django-2.2.4-green.svg)

- blog: Prrojeto desenvolvido baseado no tutorial [Try Django Tutorial (v2.2) - Build a Web Application with Python Framework](https://www.youtube.com/watch?v=0CBZenN-b6w)

-----

## Dependências

1. Instalar o [Poetry](https://poetry.eustace.io/docs/#installation) no sistema;

2. Dentro do diretório do projeto, execute:

```
$ poetry lock
$ poetry install
```

Caso queira verificar se está tudo ok, execute:

`$ poetry shell`

## Comandos do Django

- Criação do banco de dados:

`python manage.py syncdb`

- Informar ao Django que há alterações nos modelos:

`python manage.py makemigrations nome_app`

- Aplicar as mudanças realizadas ao Database:

`python manage.py migrate`

- Inicialização de um novo app:

`python manage.py startapp nome_app`

- Levantar servidor:

`python manage.py runserver`
