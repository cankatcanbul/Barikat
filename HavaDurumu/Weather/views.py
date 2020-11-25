from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
import json
import datetime

def home(request):
    return render(request, 'Weather/home.html')



# Create your views here.
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'Weather/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'Weather/signupuser.html',{'form': UserCreationForm(), 'error': 'Bu kullanıcı sisteme zaten kayıtlı'})
        else:
            return render(request, 'Weather/signupuser.html', {'form':UserCreationForm(), 'error':'Girilen Şifreler Uyuşmuyor'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'Weather/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'Weather/loginuser.html', {'form': AuthenticationForm(), 'error': 'Kullanıcı Adı veya Şifre Hatalı'})
        else:
            login(request, user)
            return redirect('currenttodos')
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def createtodo(request):
    if request.method == 'GET':

        return render(request, 'Weather/createtodo.html', {'form': TodoForm()})
    else:
        form = TodoForm(request.POST)
        global result
        global newtodo
        country = request.POST['title']
        numOfDays = request.POST['numDay']
        result = requests.get('http://api.worldweatheronline.com/premium/v1/weather.ashx?key=1e99431f9e6f443d90c123259202011&q='+country+'&format=json&num_of_days='+str(numOfDays))
        json_data = json.loads(result.text)
        request.session['myData'] = json_data
        request.session['dayN'] = numOfDays
        #newtodo = form.save(commit=False)
        #newtodo.memo = numOfDays
        #newtodo.user = request.user
        #newtodo.memo = json_data["data"]["weather"][3]["maxtempC"]

        #newtodo.save()
        return redirect('currenttodos')
        #return JsonResponse({'Weather': json_data})
        #return render(request, 'Weather/currenttodos.html', {'title': result})

@login_required
def currenttodos(request):
    try:
        jsonData = request.session['myData']
        numOfDays = request.session['dayN']
        test = "Ankarada Ortalama Sıcaklık :"+jsonData["data"]["weather"][0]["avgtempC"]+" Derece"
        CurrentTemp = jsonData["data"]["current_condition"][0]["temp_C"]
        CityName = jsonData["data"]["request"][0]["query"]
        humidtyC = jsonData["data"]["current_condition"][0]["humidity"]
        Date = []
        avgTemp = []
        FeelsLikeC = jsonData["data"]["current_condition"][0]["FeelsLikeC"]
        Weather=jsonData["data"]["current_condition"][0]["weatherDesc"][0]["value"]
        WeatherAvg= []
        Icon=jsonData["data"]["current_condition"][0]["weatherIconUrl"][0]["value"]
        timeW = []
        nextDates = []
        Day = datetime.datetime.now()
        DayList = []
        #Clock = datetime.datetime.now().strftime("%H:%M:%S")
        maxTemp = []
        minTemp=[]
        sunrise=[]
        sunset = []
        sunHour =[]
        weatherDesc=[]
        for i in range(8):  # Saatlik Hava
            timeW.append(jsonData["data"]["weather"][0]["hourly"][i]["tempC"])

        if numOfDays == "5":
            for i in range(5):
                Date.append(jsonData["data"]["weather"][i]["date"])
                avgTemp.append(jsonData["data"]["weather"][i]["avgtempC"])
                maxTemp.append(jsonData["data"]["weather"][i]["maxtempC"])
                minTemp.append(jsonData["data"]["weather"][i]["mintempC"])
                sunrise.append(jsonData["data"]["weather"][i]["astronomy"][0]["sunrise"])
                sunset.append(jsonData["data"]["weather"][i]["astronomy"][0]["sunset"])
                sunHour.append(jsonData["data"]["weather"][i]["sunHour"])
                WeatherAvg.append(jsonData["data"]["weather"][i]["hourly"][4]["weatherIconUrl"][0]["value"])
                weatherDesc.append(jsonData["data"]["weather"][i]["hourly"][4]["weatherDesc"][0]["value"])
                DayList.append(Day.strftime("%A"))
                Day += datetime.timedelta(days=1)
        else:
            for i in range(3):
                Date.append(jsonData["data"]["weather"][i]["date"])
                avgTemp.append(jsonData["data"]["weather"][i]["avgtempC"])
                maxTemp.append(jsonData["data"]["weather"][i]["maxtempC"])
                minTemp.append(jsonData["data"]["weather"][i]["mintempC"])
                sunrise.append(jsonData["data"]["weather"][i]["astronomy"][0]["sunrise"])
                sunset.append(jsonData["data"]["weather"][i]["astronomy"][0]["sunset"])
                sunHour.append(jsonData["data"]["weather"][i]["sunHour"])
                WeatherAvg.append(jsonData["data"]["weather"][i]["hourly"][4]["weatherIconUrl"][0]["value"])
                weatherDesc.append(jsonData["data"]["weather"][i]["hourly"][4]["weatherDesc"][0]["value"])
                DayList.append(Day.strftime("%A"))
                Day += datetime.timedelta(days=1)





        if request.method == 'GET':
            return render(request, 'Weather/currenttodos.html', {'test': test, 'CurrentTemp': CurrentTemp, 'CityName': CityName, 'DayList' : DayList, 'Date': Date, 'Weather': Weather, 'Icon': Icon, 'timeW': timeW, 'numOfDays':numOfDays, 'avgTemp':avgTemp, 'humidtyC': humidtyC, 'FeelsLikeC':FeelsLikeC, 'WeatherAvg':WeatherAvg, 'minTemp':minTemp, 'maxTemp':maxTemp, 'sunrise':sunrise,'sunset':sunset, 'sunHour':sunHour,'weatherDesc':weatherDesc})
    except:
        return redirect('createtodo')

