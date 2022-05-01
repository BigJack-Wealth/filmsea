
import email
from email import message
from multiprocessing import context
from pickle import FALSE
from django.shortcuts import render, redirect, get_object_or_404
from .models import Video, VideoD, Uncharted, Batman, Matrix, Morbius, Moonfall, TIB, Turn, Koati
from django.views.generic import ListView , DetailView
from .models import movie
from .models import *
import json
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

from django.core.mail import EmailMessage
from django.core.mail import send_mail



# Create your views  here.



def home(request):
    
    Index=movie.objects.all()
    return render(request, 'index_.html', {"Index":Index})

def movielist(request):
    list=movie.objects.all()
    return render(request, 'movielist.html', {"list":list})


def moviegrid(request):
    grid=movie.objects.all()
    return render(request, 'moviegrid.html', {"grid":grid})

def blog(request):
    page=movie.objects.all()
    return render(request, 'bloglist.html', {"page":page})

def pnv(request):
    com=movie.objects.all()
    return render(request, 'PnV.html', {"com":com})
#spiderman
def videod(request):
       
        videod=VideoD.objects.all()
        return render(request, 'stores/videod.html', {"videod":videod})
#uncharted
def charted(request):
       
        charted=Uncharted.objects.all()
        return render(request, 'stores/uncharted.html', {"charted":charted})
#batman
def bat(request):
       
        bat=Batman.objects.all()
        return render(request, 'stores/batman.html', {"bat":bat})
#matrix
def mat(request):
       
        mat=Matrix.objects.all()
        return render(request, 'stores/matrix.html', {"mat":mat})
#morbius    
def mob(request):
       
        mob=Morbius.objects.all()
        return render(request, 'stores/morbius.html', {"mob":mob})
#moonfall
def moon(request):
       
        moon=Moonfall.objects.all()
        return render(request, 'stores/moonfall.html', {"moon":moon})
#theinbetween
def tib(request):
       
        tib=TIB.objects.all()
        return render(request, 'stores/between.html', {"tib":tib})
#turning red
def turn(request):
       
        turn=Turn.objects.all()
        return render(request, 'stores/turningred.html', {"turn":turn})
#koati
def kot(request):
   
        kot=Koati.objects.all()
        return render(request, 'stores/koati.html', {"kot":kot})

@login_required(login_url='login')
def movie_list(request):
       
        video=Video.objects.all()
        return render(request, 'stores/movie_list.html', {"video":video})

       
def loginPage(request):
    
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       
       user = authenticate(request, username=username, password=password)
       
       if user is not None:
           login(request, user)
           return redirect('home')
       else:
           messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


# def contact(request):
        


def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            email= form.cleaned_data.get('email')
           
            form.save()
        # user = User.objects.create_user(username=username, password=password, email=email)
            
        subject = 'Thank You for signing up'
        message = 'Thank you for Signing up, it means the world to us'
        email_from = 'emmanueljack715@gmail.com' 
        recipient_list = [email,]
        
        fail_silently=False
        
        send_mail(subject, message, email_from, recipient_list)
        
        
        
        
        # send_mail(subject, message, email_from, recipient_list)
        messages.success(request, 'Account was created for ' + username)
        return redirect(loginPage)
    
    context = {'form':form}
    return render(request, 'registration/register.html', context)


# def email(request):
#         subject = 'Thank You'
#         message = 'It means'
#         email_from = settings.EMAIL_HOST_USER 
#         recipient_list = ['emmanueljack715@gmail.com',]
        
#         send_mail(subject, message, email_from, recipient_list)
#         return redirect(login)
