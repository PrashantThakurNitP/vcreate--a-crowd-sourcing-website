from django.contrib import admin
from django.urls import path,include
from .import views


from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse

urlpatterns = [

    #path("newsfeedsindia/",views.newsfeedsindia,name="newsfeedsindia"),
    #path("newsfeedsci/",views.newsfeedsci,name="newsfeedsci"),
   
    path("comp",views.comp,name="comp"),
    path("pastcontest",views.pastcontest,name="pastcontest"),
    path("livecontest",views.livecontest,name="livecontest"),
    path("organised",views.organised,name="organised"),
    path("participated",views.participated,name="participated"),
    path("viewcontest/<int:id1>",views.viewcontest,name="viewcontest"),
    path("acceptsubmission",views.acceptsubmission,name="acceptsubmission"),
    path("verifysubmission",views.verifysubmission,name="verifysubmission"),
    path("organise",views.organise,name="organisecontest"),
    path("submit/<int:contestid>",views.submit,name="submitcontest"),
    path("checkallcontest",views.checkallcontest,name="checkallcontest"),

    #path("",views.index,name="index"),









    #path('addpost/',views.addpost,name="addpost"),
]
#urlpatterns += static(settings.MEDIA_URL,
#                              document_root=settings.MEDIA_ROOT)
#urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
#urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


