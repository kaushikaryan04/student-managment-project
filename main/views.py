from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .forms import AddStudent
# from.models import AddStudent
from django.contrib.auth.decorators import login_required 


# configuring messages is pending 

def base (request):
	return render(request , "main/base.html")
	
def home(request):
	return render(request  , "main/home.html")

def login_page(request):

	return render(request ,"registration/login.html")

def register(request):
	return render(request , "registration/register.html")

def handleSignUp(request):
	if(request.method == "POST"):
		username = request.POST.get("username")
		firstName = request.POST.get("first-name")
		lastName = request.POST.get("last-name")
		email = request.POST.get("email")
		password1  = request.POST.get("password")
		password2 = request.POST.get("password2")

		if(password1 != password2):
			messages.error(request, "2 passwords do not match try again")
			return redirect("register")
		if(len(username) > 10 or len(firstName)>10 or len(lastName) > 10 and not username.isalnum()):
			messages.error(request , "very long username ")
			return redirect("register")

		myuser = User.objects.create_user(username , email , password1)
		myuser.first_name = firstName
		myuser.last_name  = lastName
		myuser.save()
		messages.success(request, "user have been added succesfully")
		return redirect("login")
	else:
		return HttpResponse("Access denied")

def handleLogin(request):
	if request.method == "POST":
		username = request.POST.get("loginUsername")
		password = request.POST.get("loginPassword")
		
		user = authenticate(username = username , password = password)
		if user is not None:
			login(request , user)
			messages.success(request, "login succesfull")
			return redirect("home")
		else:
			messages.error(request, "username or password not correct try again")
			return redirect("login")

def handleLogout(request):
	logout(request)
	messages.success(request, "logout succesfull")
	return redirect("home")


@login_required(login_url="login")
def addStudent(request):
	if request.method == 'POST':
		print(requst.POST)
		form = AddStudent(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponse("all ok")

	else:
		form = AddStudent()
	context = {"form" : form }

	return render(request , "main/addStudent.html" , context)

