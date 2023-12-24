from django.shortcuts import render
from django.Http import  HttpResponse
from . models import Feature 
# Create your views here.

def index(request):
    features = Feature.objects.all()
    feature1 = Feature
    feature1.id
    return render(request, 'index.html', {'features': features})