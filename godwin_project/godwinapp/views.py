from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context_dict = {'variable_name': 'Shark, Tilapia, Gesha,'}
    return render(request, 'godwinapp/godwin.html', context=context_dict)

def about(request):
    return HttpResponse("Welcome back to history.")