
from django.urls import path
from godwinapp import views

app_name = 'godwinapp'

urlpatterns = [
	path('', views.index, name='index'),
]
