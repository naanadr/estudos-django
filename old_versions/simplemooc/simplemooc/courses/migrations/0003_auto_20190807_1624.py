# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20190806_1653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos', 'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='course',
            name='about',
            field=models.TextField(verbose_name='Sobre o Curso', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(verbose_name='Descrição Simples', blank=True),
        ),
    ]
