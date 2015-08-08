# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):              # __unicode__ on Python 2
        return self.question_text
    

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text
    

class Entrada(models.Model):
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Todas las Entradas"
        ordering = ['-fecha']
        
    titulo = models.CharField(u'Título', max_length = 100)
    fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)
    resumen= models.CharField(u'Resumen',max_length=512)
    contenido = models.TextField(u'Contenido')
    published = models.BooleanField(u'Publicado?', default=True)
    autor = models.ForeignKey(User)
    categoria = models.ManyToManyField('Categoria')
    
    def __str__(self):
        return self.titulo
    
    
class Categoria(models.Model):
    nombre = models.CharField(u'Titulo de la Categoria', max_length=100)
    descripcion = models.CharField(u'Descripcion de la Categoria', max_length=256)
    
    
    def __str__(self):
        return self.nombre
    
    
class Contacto(models.Model):
    nombre = models.CharField(u'Nombre', max_length=100)
    celu = models.CharField(u'Telefono', max_length=100)
    mail = models.CharField(u'Mail', max_length=100)
    mensaje = models.TextField(u'Mensaje')
    fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Mensajes(models.Model):
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Todos los Comentarios"
        ordering=['-fecha']
        
    nombre = models.CharField(u'Nombre', max_length=100)
    mensaje = models.TextField(u'Mensaje')
    published = models.BooleanField(u'Publicado?', default=True)
    fecha = models.DateTimeField(u'Fecha del Mensaje', auto_now_add=True)
    published_in = models.ForeignKey(Entrada)
    
    def __str__(self):
        return self.nombre