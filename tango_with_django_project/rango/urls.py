from django.urls import path
from rango import views
from django.conf.urls import url


app_name = 'rango'

urlpatterns = [
	path('', views.index, name='index'),
	path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
	path('about/', views.about, name='about'),
	
	
]