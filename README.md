# estudos-django
[![Python Version](https://img.shields.io/badge/python-3.5.5-green.svg)](https://img.shields.io/badge/python-3.5.5-green.svg)
[![Django Version](https://img.shields.io/badge/django-1.8-green.svg)](https://img.shields.io/badge/django-1.8-green.svg)

Projeto desenvolvido baseado no curso [Python 3 na Web com Django](https://www.udemy.com/python-3-na-web-com-django-basico-intermediario/)


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

- Inicialização de um novo app:

`python manage.py startapp nome_app`

- Levantar servidor:

`python manage.py runserver`
