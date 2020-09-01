from django.shortcuts import render  
from django.template import loader  
from django.http import HttpResponseBadRequest, HttpResponse
import pandas as pd
import numpy as np
import requests
from django.shortcuts import render  

#Create your views here  
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")  

def index(request):
    return render(request,"index3.html")

def output(request):
    print('EDA')
    import subprocess
    subprocess.call(["python", "myproject/gad.py"])
    from django.http import HttpResponse
    return HttpResponse(status=204)

  





