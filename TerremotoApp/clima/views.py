from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
import requests
import json

def get_api_weather(request):
	res = requests.get('http://api.geonames.org/findNearByWeatherJSON',
		params = {'lat':'19.4284700','lng':'-99.1276600','username':'izaak'})
	if res.status_code==200:
		res = json.loads(res.text)
		print (res)
		return HttpResponse("Api de tiempo")