#from django.shortcuts import render
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.conf import settings
# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the TrainToB website.")

def get_api_data(request):
    # Example API endpoint (replace with your actual API URL and parameters)
    lat =   47.35953600
    lng = 8.63564520 
    endpoint = f"https://gateway.apiportal.ns.nl/nsapp-stations/v2/nearest?lat={lat}&lng={lng}"
    
    # API Key from settings
    headers = {
        'Ocp-Apim-Subscription-Key': settings.NS_APP_KEY
    }
    
    try:
        # Make GET request to the API
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Extract JSON response
        stations_data = response.json()
        
        # Render the data in a template (or return as JSON)
        return JsonResponse(stations_data)
    
    except requests.exceptions.RequestException as e:
        # Handle request exception
        return JsonResponse({'error': str(e)}, status=500)
    
def get_travel_data(request):
    # Example API endpoint (replace with your actual API URL and parameters)
    station = "ZUE"
    date_time = "2024-06-21T18:00:28+02:00"
    base_url = "https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2/arrivals"
    endpoint = f"{base_url}?station={station}&dateTime={date_time}"

    # API Key from settings
    headers = {
        'Ocp-Apim-Subscription-Key': settings.NS_APP_KEY
    }
    
    try:
        # Make GET request to the API
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Extract JSON response
        stations_data = response.json()
        
        # Render the data in a template (or return as JSON)
        return JsonResponse(stations_data)
    
    except requests.exceptions.RequestException as e:
        # Handle request exception
        return JsonResponse({'error': str(e)}, status=500)