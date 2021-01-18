"""udesign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path,include
#from competition import views


from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse

from django.contrib.sitemaps.views import sitemap
#from .sitemaps import feedSitemap,StaticViewSitemap,messengerSitemap,profileinfoSitemap,TodoSitemap
from django.contrib.auth import views as auth_views
from contest import views 
#from community import views as communityviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contest/', include('contest.urls')),#
    path('community/', include('community.urls')),
    path("",views.index,name="index"),
    path('logoutuser/',views.logoutuser,name="logoutuser"),
    path('signupuser/',views.signupuser,name="signupuser"),
    path('loginuser/',views.loginuser,name="loginuser"),
    #path('loginuser/',views.loginuser,name="loginuser"),
    #path("signupuser",views.signupuser,name="signupuser"),
    #path('oauth/', include('social_django.urls', namespace='social')),

    path('oauth/', include('social_django.urls', namespace='social')),
]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


