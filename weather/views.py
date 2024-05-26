from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST['city']
        res = requests.get("https://api.openweathermap.org/data/2.5/weather",
                           params={'q': city, 'appid': "22cedba8340c2053a896f40568d64fd9"})

        json_data = res.json()

        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity'])
        }
    else:
        city = ''
        data = {}

    return render(request, 'index.html', {'data': data})
