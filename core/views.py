from ast import Return
from django.shortcuts import render
import sklearn
import joblib

# Create your views here.


def home(request):
    return render(request, 'index.html')

def result(request):
    cls=joblib.load('finalized_model.sav')
    list=[]
    list.append(request.GET['RI'])
    list.append(request.GET['NA'])
    list.append(request.GET['MG'])
    list.append(request.GET['AI'])
    list.append(request.GET['SI'])
    list.append(request.GET['K'])
    list.append(request.GET['BA'])
    list.append(request.GET['CA'])
    list.append(request.GET['FE'])

    print(list)
    ans= cls.predict([list])
    
    return render(request,'result.html',{'ans':ans,'List':list})