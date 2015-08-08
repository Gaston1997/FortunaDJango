# -*- coding: utf-8 -*-

from django.conf.urls import include, url , patterns

urlpatterns=patterns('',
                     url(r'^$' , 'Blog.views.home' , name='home'),
                     url(r'^sobreyo/$' , 'Blog.views.sobreyo' , name='sobreyo'),
                     url(r'^acti/$' , 'Blog.views.acti' , name='acti'),
                     url(r'^contact/$' , 'Blog.views.contact' , name='contact'),
                     url(r'^ver_post/(?P<id_post>[0-9]+)/$', 'Blog.views.ver_post', name='vermipost'),
                     url(r'^save_message/$', 'Blog.views.save_message', name='save_message'),
                    )