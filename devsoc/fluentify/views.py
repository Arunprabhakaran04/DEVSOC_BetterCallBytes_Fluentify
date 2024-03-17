from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import requests



#To get ip address
def get_ip(request):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

#To schedule a class

def schedule_class(**kwargs):
    url = "https://api.zoom.us/v2/users/me/meetings"
    API_KEY = "YfNJ2iJqTsSa3o106aqAEg"
    API_SECRET = "Zlzpx95XWIviT3aAaXKCtDa7Zj1owUf8"
    data = {
    "topic": "My New Meeting",
    "start_time": giventime.isoformat(),
    "duration": 60,  # Duration in minutes
    "timezone": "Asia/Chennai",  
    "agenda": "My Meeting Agenda",
}
    
    

