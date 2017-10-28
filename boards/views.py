# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.http import Http404
from boards.models import Board
from django.contrib.auth import login as auth_login, authenticate, get_user_model, logout
from .forms import ExistingUserForm,UserRegisterForm,ForgotPasswordForm
from django.shortcuts import render, redirect




def home(request):
	boards = Board.objects.all()
	return render(request,'home.html',{'boards': boards})

def board_topics(request, pk):
    # try:
    #     board = Board.objects.get(pk=pk)
    # except:
    #     raise Http404

    board = get_object_or_404(pk=pk)
    return render(request, 'topics.html', {'board': board})

def table(request):
	return render(request,'table.html')

def dashboard(request):
	return render(request,'dashboard.html')

def icons(request):
	return render(request,'icons.html')

def maps(request):
	return render(request,'maps.html')

def notifications(request):
	return render(request,'notifications.html')

def index(request):
	return render(request,'index.html')

def calendar(request):
	return render(request,'calendar.html')	

def supreme_details(request):
	return render(request,'supremecourtdetails.html')

def highcourtdetails(request):
	return render(request,'highcourtdetails.html')

def districtcourtdetails(request):
	return render(request,'districtcourtdetails.html')

def login(request):
	# form = ExistingUserForm(request.POST or None)
	# if form.is_valid():
	# 	username = form.cleaned_data.get('username')
	#  	password = form.cleaned_data.get('password')
	#  	user = authenticate(username=username,password=password)
	#  	auth_login(request,user)
	#  	print(request.user.is_authenticated())
	#  	return HttpResponseRedirect('/register/success/')
	#  else:
	#  	form = ExistingUserForm()
	#  	print "Hello"
	form = ExistingUserForm()
	return render(request,"login.html",{"form":form})


def forgotpassword(request):
	form = ForgotPasswordForm()
	return render(request,'forgotpassword.html',{"form":form})

def change_password(request):
	return render(request,'change_password.html')

def registeration(request):
	form = UserRegisterForm()

	# context = {

	# 		"form" : form,

	# }
	return render(request,'registeration.html',{"form":form})

def logout(request):
	logout(request)
	return render(request,'logout.html')

def welcome_email(request):
	return render(request,'welcome_email.html')

def landing_page(request):
	return render(request,'landing_page.html')

