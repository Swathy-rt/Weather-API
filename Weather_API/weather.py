import requests

from datetime import datetime

api_key = '482190a7c86f2bbaec16da435ecbf67b'
location = input("Enter the city : ")

#complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key

# mine -> api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# https://api.openweathermap.org/data/2.5/weather?q=ranchi&appid=482190a7c86f2bbaec16da435ecbf67b
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
print(complete_api_link)
api_link = requests.get(complete_api_link)
#print(api_link)      #respnse object return
api_data = api_link.json() # data key seperate json object
print(api_data)


#create variables
temperature = ((api_data['main']['temp']) - 273.15) # temperature fetch ddegre celcius
#print(city)
weather = api_data['weather'][0]['description']
#print(weather)
longitude = api_data['coord']['lon']
#print(longitude)
humidity = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
print("                ")
print("Weather Status of {} city ".format(location))

print("Temperature : {} in degree Celcius: ".format(temperature))
print("Weather : ",weather)
print("Humiity : ",humidity)
print("Wind speed : ",wind_speed," kmph")



