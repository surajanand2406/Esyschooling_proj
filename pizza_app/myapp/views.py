from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView
from .forms import CreateForm
from .models import OrderYourPizza


class home(TemplateView):
	template_name = "myapp/home.html"


def SignUp(request):
	if request.method == 'GET':
		return render(request, 'myapp/register.html', {'form':UserForm()})
	else:
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('home')
			except IntegrityError:
				return render(request, 'myapp/register.html', {'form':UserForm(), 'error':'Username already exist'})
		else:
			return render(request, 'myapp/register.html', {'form':UserForm(), 'error':'Password did not match'})

def LogIn(request):
	if request.method == 'GET':
		return render(request, 'myapp/login.html', {'form':AuthenticationForm()})
	else:
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is None:
			return render(request, 'myapp/login.html', {'form':AuthenticationForm(), 'error':'username and password not exist'})
		else:
			login(request, user)
			return redirect('home')

def LogOut(request):
	return render(request, 'myapp/logout.html')


def CreatePizza(request):
	if request.method == 'GET':
		return render(request, 'myapp/create.html', {'form':CreateForm()})
	else:
		form = CreateForm(request.POST)
		newpizza = form.save(commit=False)
		newpizza.user = request.user
		newpizza.save()
		return redirect('detail')

def UpdateView(request, myapp_pk):
	updated_pizza = get_object_or_404(OrderYourPizza, pk=myapp_pk, user=request.user)
	form = CreateForm(instance=updated_pizza)
	return render(request, 'myapp/update.html', {'updated_pizza':updated_pizza, 'form':form})

def PizzaDetails(request):
	details = OrderYourPizza.objects.filter(user=request.user)
	return render(request, 'myapp/detail.html', {'details': details})



def DeleteView(request, myapp_pk):
	updated_pizza = get_object_or_404(OrderYourPizza, pk=myapp_pk, user=request.user)
	if request.method =='POST':
		updated_pizza.delete()
		return redirect('detail')
