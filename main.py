from tkinter import messagebox
import requests
from tkinter import *

window = Tk()
window.title("Weather Report")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

api_key = 'API-KEY'


label = Label(text="Please choose a city")
label.config(bg="black", fg="white", border="10px")
label.pack()

def listbox_selected(event):
    city = my_listbox.get(my_listbox.curselection())
    weather_report(city)

my_listbox = Listbox(height=35, width=40)  # Increased the size of the listbox

name_list = ["Istanbul", "London", "New York", "Tokyo", "Paris", "Beijing", "Moscow", "Dubai",
             "Los Angeles", "Sydney", "Berlin", "Rome", "Cairo", "Mumbai", "Seoul", "Mexico City", "Toronto",
             "New Delhi", "Bangkok", "Rio de Janeiro", "Cape Town", "Stockholm", "Amsterdam", "Athens", "Prague",
             "Vienna", "Budapest", "Zurich", "Oslo", "Helsinki", "Warsaw", "Lisbon", "Madrid", "Barcelona",
             "Brussels", "Copenhagen", "Dublin", "Edinburgh", "Geneva", "Luxembourg", "Monaco", "Nice", "Naples",
             "Sydney", "Melbourne", "Auckland", "Wellington", "Vancouver", "Montreal", "Calgary", "Edmonton"]

for i in range(len(name_list)):
    my_listbox.insert(i, name_list[i])

my_listbox.bind('<<ListboxSelect>>', listbox_selected)
my_listbox.pack()

def radio_selected():
    print(radio_checked_state.get())

radio_checked_state = IntVar()

# Create a frame for the radio buttons
radio_frame = Frame(window)
radio_frame.pack()

celsius_radio = Radiobutton(radio_frame, text="Celsius", value=10, variable=radio_checked_state)
kelvin_radio = Radiobutton(radio_frame, text="Kelvin", value=20, variable=radio_checked_state)
fahrenheit_radio = Radiobutton(radio_frame, text="Fahrenheit", value=30, variable=radio_checked_state)

# Pack the radio buttons in the frame with side and padx parameters
celsius_radio.pack(side=LEFT, padx=5)
kelvin_radio.pack(side=LEFT, padx=5)
fahrenheit_radio.pack(side=LEFT, padx=5)

def weather_report(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']

        # Get the selected temperature unit
        selected_unit = radio_checked_state.get()

        if selected_unit == 10:  # Celsius
            temperature = round(temp - 273.15, 3)
            unit_label = "°C"
        elif selected_unit == 20:  # Kelvin
            temperature = round(temp, 3)
            unit_label = "K"
        elif selected_unit == 30:  # Fahrenheit
            temperature = round((temp - 273.15) * 9 / 5 + 32, 3)
            unit_label = "°F"
        else:  # nothing
            temperature = round(temp - 273.15, 3)
            unit_label = "°C"
        # Display temperature and description in a messagebox
        messagebox.showinfo(
            title="Weather Report",
            message=f'Temperature: {temperature} {unit_label}\nDescription: {desc}'
        )
    else:
        error_message = f"Error fetching weather data for {city}. Please try again later."
        print(error_message)
        messagebox.showerror(title="Error", message=error_message)

window.mainloop()
