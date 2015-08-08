# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Titulo de la Categoria')),
                ('descripcion', models.CharField(max_length=256, verbose_name='Descripcion de la Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Post')),
                ('mensaje', models.TextField(verbose_name='Contenido')),
            ],
            options={
                'ordering': ['-fecha'],
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('celu', models.CharField(max_length=100, verbose_name='Telefono')),
                ('mail', models.CharField(max_length=100, verbose_name='Mail')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Post')),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Post')),
                ('resumen', models.CharField(max_length=512, verbose_name='Resumen')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('published', models.BooleanField(default=True, verbose_name='Publicado?')),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ManyToManyField(to='Blog.Categoria')),
            ],
            options={
                'ordering': ['-fecha'],
                'verbose_name': 'Mi Entrada',
                'verbose_name_plural': 'Todas mis entradas',
            },
        ),
        migrations.AddField(
            model_name='comentario',
            name='entrada',
            field=models.ForeignKey(to='Blog.Entrada'),
        ),
    ]
