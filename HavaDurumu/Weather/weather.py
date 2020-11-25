
import requests
import json
import datetime
dt = datetime.datetime.today()
result = requests.get('http://api.worldweatheronline.com/premium/v1/weather.ashx?key=1e99431f9e6f443d90c123259202011&q=London&format=json&num_of_days=5')

json_data = json.loads(result.text)
havaVar = json_data["data"]["current_condition"][0]["weatherDesc"][0]["value"]
 #json_data["data"]["current_condition"][0]["FeelsLikeC"]
 #FeelsLikeC
print(json_data["data"]["weather"][3]["maxtempC"])

print("Şu anda Hava "+json_data["data"]["current_condition"][0]["temp_C"]+" Derece") # Anlık Derece
print(json_data["data"]["request"][0]["query"]) # Şehrin Adı


print(json_data["data"]["weather"][3]["maxtempC"])

print("Şu anda hava " + json_data["data"]["current_condition"][0]["weatherDesc"][0]["value"] ) # Anlık Hava

#if json_data["data"]["current_condition"][0]["weatherDesc"][0]["value"] == "Partly cloudy":
    #havaVar = "Parcalı Bulutlu"

print("Şu anda hava " + json_data["data"]["current_condition"][0]["weatherIconUrl"][0]["value"] )  # İcon

print(json_data["data"]["weather"][0]["date"]) # Tarih

now = datetime.datetime.now()
print(now.strftime("%A"))
#print("Şu anda hava " + havaVar)

for i in range(8): # Saatlik Hava
    print(json_data["data"]["weather"][0]["hourly"][i]["time"]+" saatinde Hava :"+json_data["data"]["weather"][0]["hourly"][i]["tempC"])

for i in range(5):  # Saatlik Hava
        print(json_data["data"]["weather"][i]["date"] + " Tarihinde Ortalama Sıcaklık :" + json_data["data"]["weather"][i]["avgtempC"] + " Derece ")


    #Day = datetime.datetime.now()
    #Day = Day.strftime("%A")

Day = datetime.datetime.now()
DayList = []
WeatherAvg = []
for i in range(5):
    #print(Day.strftime("%A"))
    Day += datetime.timedelta(days=1)
    DayList.append(Day.strftime("%A"))
    WeatherAvg = json_data["data"]["weather"][i]["hourly"][4]["weatherIconUrl"][0]["value"]
    print(json_data["data"]["weather"][i]["astronomy"][0]["sunrise"])
#print(WeatherAvg)



#print(DayList)