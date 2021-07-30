
from django.urls import path
from godwinapp import views

app_name = 'godwinapp'

urlpatterns = [
	path('', views.godwin, name='godwin'),
	path('history/', views.history, name='history'),
]
