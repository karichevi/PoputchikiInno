from django.http import HttpResponseRedirect, response
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
# Create your views here.
from rest_framework import viewsets  # add this
from django.contrib.auth.models import User
#from .serializers import UserSerializer
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User as A_user
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import ProfileSignupForm , ProfileLogInForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
import json
from .models import Profile
import ast
from django.contrib.auth import authenticate

User = get_user_model()

class LogOutView(generic.DetailView):
    model = User
    template_name = 'user/logout.html'


def home(request):
    content = {
            'status' : 'request was permitted'
        }
    return render(request, 'user/home.html', content)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        #data = ast.literal_eval(request.body.decode())
        u_name = request.POST.get('username')
        u_pass = request.POST.get('password')
        print(u_name, u_pass )
        user = authenticate(username=u_name, password=u_pass)
        if user is not None:
            return JsonResponse({'token': data['username']})
        else:
            return JsonResponse({'token': ''})
    else:
        form = ProfileLogInForm()
    return render(request, 'user/login.html', {'form' : form})

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = ast.literal_eval(request.body.decode())
        user = Profile.objects.create_user(username=data['username'],
                                           password=data['password'],
                                           first_name=data['first_name'],
                                           last_name=data['last_name'],
                                           email=data['email'],
                                           mobile_number=data['mobile_number'])
        return JsonResponse({'token': user.username})
    else :
        form = ProfileSignupForm()
    return render(request , 'user/signup.html' , {'form': form})


def logout(request, user_id):
    return render(request, 'user/logout.html', {'data': 'data'})


