from django.shortcuts import render, redirect
from .models import *

#login
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def affichage(request):
    return render(request, 'indexkivu.html')

def affichage_apropos(request):
    return render(request, 'apropos.html')

def affichage_service_pann(request):
    return render(request, 'service_panneau.html')

def affichage_contact(request):
    return render(request, 'contactkivu.html')

def affichage_service(request):
    return render(request, 'servicekivu.html')

def affichage_projetkivu(request):
    return render(request, 'projetskivu.html')

def affichage_form(request):
    return render(request, 'form.html')





#create contact
def AfficheDemande(request):
    contact=Contact.objects.all()
    context={
        'contact':contact
    }
    return render(request, 'contactkivu.html', context)

    

    #début crud contact 
def createContact(request):
    if request.method=="POST":
        nom = request.POST.get('nom')
        mail = request.POST.get('mail')
        adresse = request.POST.get('adresse')
        numtel = request.POST.get('numtel')
        message = request.POST.get('message')

        form = Contact(
        nom=nom,
        mail=mail,
        adresse=adresse,
        numtel=numtel,
        message=message
        
            )

        form.save()
        return redirect('contact')

def supprimerContact(request, pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return redirect('contact')
#fin ajout d'un contact


#debut ajout d'une nouvelle formation
def createform(request):
    if request.method=="POST":
        photo = request.FILES['photo'] or None
        description = request.POST.get('description')
    
        form = News.objects.create(
        photo=photo,
        description=description,
        )

        form.save()
        return redirect('form')
    return render(request, 'form.html')


def Affiche_projet(request):
    news=News.objects.all()
    context={
        'news':news
    }
    return render(request, 'projetskivu.html', context)

def supprimerform(request, pk):
    form = News.objects.get(id=pk)
    form.delete()
    return redirect('form')








