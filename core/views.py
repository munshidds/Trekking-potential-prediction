from ast import Return
from django.shortcuts import render
import sklearn
import joblib
import numpy as np

# Create your views here.


def home(request):
    return render(request, 'index.html')

def result(request):

    list=[]
    list.append(request.GET['Age'])
    list.append(request.GET["solo/team"])
    list.append(request.GET['gender'])
    list.append(request.GET["smoker/not"])
    list.append(request.GET["Jeep_serviece"])
    list.append(request.GET["food_habit"])
    list.append(request.GET["exersice"])
    list.append(request.GET["climate"])




    list2=[]

    list2.append(request.GET['Age'])
    if request.GET['solo/team']== "Team":
        list2.append(1)
    elif request.GET['solo/team']== 'Solo':
        list2.append(0)

    
    if request.GET['gender']=='Male':
        list2.append(1)
    elif request.GET['gender']=='Female':
        list2.append(0.5)



    if request.GET["smoker/not"]=='I do smoke':
        list2.append(0)
    elif request.GET["smoker/not"]== "I don't smoke":
        list2.append(1)

    
    if request.GET['Jeep_serviece']=='I need vehicle':
        list2.append(2)
    elif request.GET["Jeep_serviece"]=="I don't need vehicle":
        list2.append(0)

    
    if request.GET['food_habit']=='Homely food':
        list2.append(1)
    elif request.GET['food_habit']=='Fast food':
        list2.append(0)


    if request.GET["exersice"]=='I do exercise':
        list2.append(1)
    elif request.GET["exersice"]=="I don't exercise":
        list2.append(0)

    
    if request.GET['climate']=='Hot':
        list2.append(1)
    elif request.GET['climate']=='Rainy':
        list2.append(0)


 

    model1=joblib.load('capability_prediction.sav')
    ans1=model1.predict([list2])
    if ans1=='yes':
        ans2='Hiii .. Congratulations, You are able to do this trekking'
    else:
        ans2='Hiii ... , You are NOT eligible for this trekking'

    model2=joblib.load('feed_back_model.sav')
    ans3=model2.predict([list2])


   
    
    return render(request,'result.html',{'list':list,"ans2":ans2,'ans3':ans3})