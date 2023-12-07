from django.shortcuts import render, redirect
from . import models
# from app2.models import MyModel

# Create your views here.

def home(request):
    mymodel = models.MyModel.objects.all()
    # print(mymodel)
    return render(request, 'home.html', {'data' : mymodel})

def detete_M(requst, id_no):
    Mmdl = models.MyModel.objects.get(pk = id_no).delete()
    # print(Mmdl)
    return redirect("homepage")

def about(request):
    return render(request, 'about.html')
