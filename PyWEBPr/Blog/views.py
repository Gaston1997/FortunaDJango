# -*- coding: utf-8 -*-


from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from Blog.models import Entrada , Contacto ,  Mensajes
from django.core.mail import EmailMessage

# Create your views here.

def home(request):
    context = RequestContext(request)
    posts = Entrada.objects.filter(published = True)
    return render_to_response('home.html', 
                              {'posts':posts},
                              context)

def ver_post(request,id_post):
    context = RequestContext(request)
    mi_post = Entrada.objects.get(id = id_post)
    mensajes = Mensajes.objects.filter(published_in = mi_post, published = True)

    return render_to_response('post.html',
                              {'post':mi_post,
                               'mensajes':mensajes},
                              context)

def sobreyo(request):
    context = RequestContext(request)
    return render_to_response('sobreyo.html' , context)

def acti(request):
    context = RequestContext(request)
    return render_to_response('acti.html' , context)

def contact(request):
    context = RequestContext(request)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        suger = request.POST['sugerencia']
        mensaje= request.POST['descripcion']
        email = EmailMessage(nombre+' te ha enviado un mail Gaston', 'Sugerencia/Opinion: '+suger+"\n\n"+mensaje, to=['fortunagaston123@gmail.com'])
        email.send()
        
    return render_to_response('contact.html', 
                              context)

def save_message(request):
    context = RequestContext(request)
    mensajes = None
    if request.method == 'POST':
        mi_post = Entrada.objects.get(id=request.POST['id'])
        nombre= request.POST['nombre']
        mensaje= request.POST['mensaje']        
        msje = Mensajes()
        msje.nombre = nombre
        msje.mensaje = mensaje
        msje.published_in = mi_post
        msje.save()
        mensajes = Mensajes.objects.filter(published_in=mi_post, published = True)

        return render_to_response('mensajes.html', 
                                  {'mensajes':mensajes},
                                  context)