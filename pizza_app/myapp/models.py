from django.db import models
from django.contrib.auth.models import User

class OrderYourPizza(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	Type = models.CharField(max_length=7)
	Size = models.CharField(max_length=6)
	Topping = models.CharField(max_length=10)

	def __str__(self):
		return self.Type


