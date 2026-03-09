import webbrowser
import datetime
import os
import requests
import urllib.parse
import pywhatkit
from googlesearch import search
import pyautogui
import psutil
import speedtest
# ---------------------------
# Open Websites
# ---------------------------

def open_youtube():
    webbrowser.open("https://youtube.com")


def open_youtube_search(query):
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")


def play_youtube(query):
    pywhatkit.playonyt(query)


def open_google():
    webbrowser.open("https://google.com")


def search_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")


# ---------------------------
# Time
# ---------------------------

def tell_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M")


# ---------------------------
# Open Applications
# ---------------------------

def open_app(command):
    os.system(command)


# ---------------------------
# Music
# ---------------------------

def play_music(folder):
    try:
        songs = os.listdir(folder)
        if songs:
            os.startfile(os.path.join(folder, songs[0]))
    except:
        pass


# ---------------------------
# Notes
# ---------------------------

def create_note(text):
    with open("notes.txt", "a") as f:
        f.write(text + "\n")


# ---------------------------
# Weather
# ---------------------------

API_KEY = "1d5e39ce9215dc9a7c1f8c8a7886eaf6"


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    data = requests.get(url).json()

    if "main" not in data:
        return "Sorry, I could not get the weather."

    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    return f"The weather in {city.title()} is {round(temp)} degrees Celsius with {weather}"


# ---------------------------
# google search
# ---------------------------

def google_search(query):
    try:
        import webbrowser
        import urllib.parse

        query = urllib.parse.quote(query)
        url = f"https://www.google.com/search?q={query}"

        webbrowser.open(url)

        return "Opening Google results."

    except Exception as e:
        print(e)
        return "Something went wrong while searching Google."
# ---------------------------
# Maps
# ---------------------------

def open_maps():
    webbrowser.open("https://maps.google.com")


def search_place(place):
    webbrowser.open(f"https://www.google.com/maps/search/{place}")


def direction_to(place):
    place = urllib.parse.quote(place)
    url = f"https://www.google.com/maps/dir/?api=1&destination={place}"
    webbrowser.open(url)


def my_location():
    webbrowser.open("https://www.google.com/maps")


# ---------------------------
# Screenshot
# ---------------------------

def take_screenshot():
    file = "screenshot.png"
    img = pyautogui.screenshot()
    img.save(file)
    return "Screenshot captured."


# ---------------------------
# Power Controls
# ---------------------------

def shutdown_pc():
    os.system("shutdown /s /t 1")


def restart_pc():
    os.system("shutdown /r /t 1")


def lock_pc():
    os.system("rundll32 user32.dll,LockWorkStation")

def system_status():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    return  f"CPU usage is {cpu} percent and memory usage is {ram} percent"

def internet_speed():
    st = speedtest.Speedtest()
    download = st.download() / 1_000_000
    upload = st.upload() / 1_000_000

    return f"Download speed is {round(download)} Mbps and upload speed is {round(upload)} Mbps"

def battery_status():
    battery = psutil.sensors_battery()

    if battery:
        percent = battery.percent
        return f"Battery is at {percent} percent"
    else:
        return "Battery information not available"
    
def volume_up():
    for _ in range(10):
        pyautogui.press("volumeup")
    return "Increasing volume"


def volume_down():
    pyautogui.press("volumedown")
    return "Decreasing volume"


def mute_volume():
    pyautogui.press("volumemute")
    return "Muting volume"



    
