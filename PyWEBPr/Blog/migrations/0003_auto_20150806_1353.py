# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20150803_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('published', models.BooleanField(default=True, verbose_name='Publicado?')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Mensaje')),
            ],
            options={
                'ordering': ['-fecha'],
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Todos los mensajes',
            },
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='entrada',
        ),
        migrations.AlterModelOptions(
            name='entrada',
            options={'ordering': ['-fecha'], 'verbose_name': 'Entrada', 'verbose_name_plural': 'Todas las Entradas'},
        ),
        migrations.AlterField(
            model_name='entrada',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='T\xedtulo'),
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
        migrations.AddField(
            model_name='mensajes',
            name='published_in',
            field=models.ForeignKey(to='Blog.Entrada'),
        ),
    ]
