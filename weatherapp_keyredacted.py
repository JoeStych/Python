from ast import Lambda
import tkinter as tk
from tkinter import font
import requests

HEIGHT = 420
WIDTH = 720
UNIT = "imperial"

#[KEY] marks where my personal openweather key is used. Get your own key free at their site below.
#openweathermap.org

def findWeather(entry):
    weather_key = '[KEY]'
    url = "api.openweathermap.org/data/2.5/forecast"
    params = {'APPID': weather_key, 'q': entry, 'units': 'Imperial'}
    response = requests.get("http://api.openweathermap.org/geo/1.0/direct?q=" + entry + "&limit=1&appid=[KEY]")
    #print(response.json())
    json_load = response.json()
    lat = json_load[0]['lat']
    lon = json_load[0]['lon']
    
    print(lat, lon)
    
    global UNIT
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&units=" + UNIT + "&appid=[KEY]")
    
    json_load = response.json()
    try:
        temp = json_load['main']['temp']
        weather = json_load['weather'][0]['description']
        name = json_load['name']
        windSpeed = json_load['wind']['speed']
        windDir = json_load['wind']['deg']
        feelslike = json_load['main']['feels_like']
        
        if windDir > 23 and windDir <= 68:
            windDir = "NE"
        elif windDir > 68 and windDir <= 113:
            windDir = "E"
        elif windDir > 113 and windDir <= 158:
            windDir = "SE"
        elif windDir > 158 and windDir <= 203:
            windDir = "S"
        elif windDir > 203 and windDir <= 248:
            windDir = "SW"
        elif windDir > 248 and windDir <= 293:
            windDir = "W"
        elif windDir > 293 and windDir <= 338:
            windDir = "NW"
        else:
            windDir = "N"
        
        if UNIT == "imperial":
            final = name + "\nCurrent Weather: " + weather + '\nTemperture: ' + str(temp) + " °F\nFeels like: " + str(feelslike) + " °F\nWindSpeed: " + str(windSpeed) + "mph " + windDir
        else:
            final = name + "\nCurrent Weather: " + weather + '\nTemperture: ' + str(temp) + " °C\nFeels like: " + str(feelslike) + " °C\nWindSpeed: " + str(windSpeed) + "kmph " + windDir
            
    except:
        final = "There was a problem retrieving the requested information."
    
    label['text'] = final
    print(json_load)

    
def changeUnits():
    global UNIT
    if UNIT == "imperial":
        unitButton['text'] = "Metric"
        UNIT = "metric"
    else:
        unitButton['text'] = "Imperial"
        UNIT = "imperial"


root = tk.Tk()

root.geometry("1080x720")

canvas = tk.Canvas(root, bg='white', height=HEIGHT, width=WIDTH)
canvas.place(relheight=1, relwidth=1)

background = tk.PhotoImage(file="sunny-sky-generic.png")
background_label = tk.Label(canvas, image=background)
background_label.place(relwidth=1, relheight=1)

frame1 = tk.Frame(root, bg='#b3e6ff', highlightthickness=2, highlightbackground="black")
frame1.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.1)

frame2 = tk.Frame(root, bg='#b3e6ff', highlightbackground="black", highlightthickness=2)
frame2.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.5)

entry = tk.Entry(frame1, bg='#e0e0d2', font=40)
entry.place(relx=0.05, rely=0.1, relheight=0.8, relwidth=0.55)

button = tk.Button(frame1, bg='#e0e0d2', text="Search Weather", font=40, command= lambda: findWeather(entry.get()))
button.place(relx=0.7, rely=0.1, relheight=0.4, relwidth=0.2)

unitButton = tk.Button(frame1, bg="#e0e0d2", text="Imperial", font=40, command=changeUnits)
unitButton.place(relx=0.7, rely=0.55, relheight=0.4, relwidth=0.2)

label = tk.Label(frame2, bg='white', font = ('Roland', 20))
label.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

root.mainloop()