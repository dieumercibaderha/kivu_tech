"""
URL configuration for kivutech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from kivutech_app.views import *
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', affichage,name="acceuil"),
    path('apropos', affichage_apropos,name="apropos"),
    path('servicepan', affichage_service_pann,name="servicepan"),
    path('contact', affichage_contact,name="contact"), 
    path('service', affichage_service,name="service"),
    path('demande',AfficheDemande,name="demande"),
    path('projet', Affiche_projet,name="projet"),
    


    path('create', createContact, name='create'),
    path('form', createform,name="form"),
    path('supprimer', supprimerContact, name='supprimer'),
    path('supprimerform', supprimerform, name='supprimerform'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
