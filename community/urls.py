from django.contrib import admin
from django.urls import path,include
from .import views


from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse

urlpatterns = [

    #path("newsfeedsindia/",views.newsfeedsindia,name="newsfeedsindia"),
    #path("newsfeedsci/",views.newsfeedsci,name="newsfeedsci"),
   
    path("",views.community,name="community"),
    path("about",views.about,name="about"),


    ]
   
#urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
