import tkinter as tk
import requests

def format_response(weather):
    try:
        name = weather['name']
        country = weather['sys']['country']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        tempmin = weather['main']['temp_min']
        tempmax = weather['main']['temp_max']
        feelslike = weather['main']['feels_like']
        humidity = weather['main']['humidity']
        pressure = weather['main']['pressure']
        windspeed = weather['wind']['speed']
        winddeg = weather['wind']['deg']
        visibility = weather['visibility']

        final_str = 'City: %s \nCountry: %s \nConditions: %s \nTemperature (°C): %s \nMin Temperature (°C): %s \nMax ' \
                    'Temperature (°C): %s \nFeels Like (°C): %s \nHumidity : %s%% \nPressure: %s mb \nWind Speed: %s ' \
                    'meter/sec \nWind Degree: %s° \nVisibility: %s meters' % (
                        name, country, desc, temp, tempmin, tempmax, feelslike, humidity, pressure, windspeed, winddeg,
                        visibility)
    except:
        final_str = 'There was a problem retrieving that\ninfo.\n\nPlease enter city name again or zip\ncode again.'

    return final_str

def get_weather(city):
    weather_key = 'f81531c787785da7aba874a6b746f65c'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

HEIGHT = 500
WIDTH = 600

root = tk.Tk()
root.resizable(False, False)
root.title('Weather App')

icon = tk.PhotoImage(file='weather-app.png')

root.iconphoto(False, icon)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 15), justify='left')
entry.insert(0, "Enter city name")
entry.place(relwidth=0.65, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, justify='left', anchor='w', font=('Courier', 15))
label.place(relwidth=1, relheight=1)

# Get weather button
button = tk.Button(frame, text="Get Weather", font=('Courier', 14), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

# Main Loop
root.mainloop()
