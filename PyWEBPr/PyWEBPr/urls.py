from django.conf.urls import include, url
from django.contrib import admin
from Blog import views

urlpatterns = [

    url(r'^', include('Blog.urls',namespace= "PyWEB")),
    url(r'^admin/', include(admin.site.urls)),
]
