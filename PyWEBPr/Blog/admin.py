# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Question, Entrada, Categoria, Contacto, Mensajes
admin.site.register(Question)

admin.site.register(Entrada)
admin.site.register(Categoria)
admin.site.register(Contacto)
admin.site.register(Mensajes)