from django.forms import ModelForm
from .models import OrderYourPizza
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateForm(ModelForm):
	class Meta:
		model = OrderYourPizza
		fields = ['Type', 'Size', 'Topping']



class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','password1','password2']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].label = 'Enter Username'
		self.fields['password1'].label = 'Password'
		self.fields['password2'].label = 'Confirm Password'