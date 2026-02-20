import requests

API_KEY = "4e8f28b476c0fab3b9fa02491fb03009"

lat = 27.9881
lon = 86.9250

url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}" 
response = requests.get(url) 
data = response.json() 
# Extract AQI  
aqi = data['list'][0]['main']['aqi'] 
# AQI scale (1=Good, 2=Fair, 3=Moderate, 4=Poor, 5=Very Poor) 
print("AQI:", aqi)