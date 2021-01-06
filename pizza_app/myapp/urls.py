from django.urls import path
from myapp import views

urlpatterns = [
	path('', views.home.as_view(), name='home'),
	path('create/', views.CreatePizza, name='create'),
	path('details/', views.PizzaDetails, name='detail'),
	path('signup/', views.SignUp, name='signup'),
	path('login/', views.LogIn, name='login'),
	path('logout/', views.LogOut, name='logout'),
	path('update_pizza/<int:myapp_pk>/', views.UpdateView, name='update'),
	path('delete_pizza/<int:myapp_pk>/', views.DeleteView, name='delete'),
 
]