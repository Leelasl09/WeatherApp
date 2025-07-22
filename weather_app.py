import requests
from tkinter import *

def get_weather():
    city = city_entry.get()
    api_key = "3f83696b5ac70247d3ef4afa05ba91d8"  # <-- Make sure you replaced it with your real key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    weather_info = response.json()
    print(weather_info)

    if weather_info.get("cod") != 200:
        result_label.config(text="City not found or API error")
    else:
        temp = weather_info['main']['temp']
        condition = weather_info['weather'][0]['description']
        result = f"Temperature: {temp}°C\nCondition: {condition.capitalize()}"
        result_label.config(text=result)

# Tkinter GUI
root = Tk()
root.title("Weather App")

city_entry = Entry(root)
city_entry.pack(pady=10)

btn = Button(root, text="Get Weather", command=get_weather)
btn.pack(pady=5)

result_label = Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()