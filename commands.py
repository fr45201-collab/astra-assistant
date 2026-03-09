from voice import speak
import system
import memory
import datetime

last_topic = None

def handler(command):
    global last_topic
    command = command.lower()

    if "open youtube" in command:
        speak("Opening YouTube")
        query = command.replace("open youtube", "").strip()

        if query:
            speak(f"Opening Youtube and searching {query}")
            system.open_youtube_search(query)
        else:
            speak("Opening YouTube")
            system.open_youtube()

    elif "open google" in command:
        speak("Opening Google")
        system.open_google()

    elif "search" in command:
        query = command.replace("search", "")
        speak("Searching Google")
        system.search_google(query)

    elif "time" in command:
        time = system.tell_time()
        speak(f"The time is {time}")

    elif "open chrome" in command:
        speak("Opening Chrome")
        system.open_app("start chrome")

    elif "open vscode" in command:
        speak("Opening VS Code")
        system.open_app("code")

    elif "play music" in command:
        speak("Playing Music")
        system.play_music("music")

    elif "remember" in command:
        text = command.replace("astra", "").replace("remember", "").strip()

        if " is " in text:
            key, value = text.split(" is ", 1)
            memory.remember(key.strip().lower(), value.strip())
            speak("Okay, I will remember that.")
        else:
            speak("Please say it like: remember something is something.")

    elif command.startswith("whay is"):
        key = command.replace("what is", "").strip()

        value = memory.recall(key)

        if value:
            speak(f"{key} is {value}")
        else:
            speak("I do not remember that yet.")

    elif "note" in command:
        text = command.replace("note", "")
        system.create_note(text)
        speak("Note saved")

    elif "who created you" in command:
        speak("I was created by Faizan Raza, a developer who loves programming and building intelligence systems.")

    elif "open github" in command:
        speak("Opening GitHub profile")
        system.open_app("start https://github.com/fr45201-collab")

    elif "weather" in command:
        city = command.replace("weather", "").strip()

        if city == "":
            city = "Delhi"

        result = system.get_weather(city)
        speak(result)

    elif "tell me about myself" in command:
        speak("You are Faizan Raza. You are learning programming and building your own assistant called Astra")

    elif "who are you" in command:
        speak("I am Astra, your personal assistant")

    elif "how are you" in command:
        speak("I am functioning perfectly. Thanks for asking")

    elif "tell a joke" in command:
        speak("Why do programmers prefer dark mode? Because light attracts bugs.")

    elif "start coding mode" in command:
        speak("Opening coding environment")
        system.open_app("code")

    elif "motivate me" in command:
        speak("Remember Faizan, every expert was once a beginner. Keep building.")

    elif "play" in command and "youtube" in command:
        query = command.replace("play", "").replace("youtube", "").strip()

        if query:
            speak(f"Playing {query} on Youtube")
            system.play_youtube(query)
        else:
            speak("What should I play?")

    elif "open maps" in command:
        speak("Opening Google Maps")
        system.open_maps()

    elif "where is" in command:
        place = command.replace("where is", "").strip()
        speak(f"Showing location of {place}")
        system.search_place(place)

    elif "near me" in command:
        place = command.replace("near me", "").strip()
        speak(f"Searching for {place} near you")
        system.search_place(place + " near me")

    elif "direction to" in command:
        place = command.replace("direction to", "").strip()
        speak(f"Getting direction to {place}")
        system.direction_to(place)

    elif "where am i" in command or "my location" in command:
        speak("Showing your current location")
        system.my_location()

    elif "who is" in command:
        query = command.replace("who is", "").strip()

        last_topic = query

        speak("searching Google")
        result = system.google_search(query)
        speak(result)

    elif "tell me more" in command or "more" in command:
        
        if last_topic:
            speak(f"Searching more about{last_topic}")
            result = system.search_wikipedia(last_topic)
            speak(result)
        else:
            speak("I do not knwo what topic you are referring to.")

    elif "what is" in command:
        key = command.replace("astra", "").replace("what is", "").strip()
        
        last_topic = key
        value = memory.recall(key)

        if value:
            speak(f"{key} is {value}")
        else:
            speak("Searching Google")
            result = system.google_search(key)
            speak(result)

    elif "shutdown computer" in command:
        speak("Shutting down the computer")
        system.shutdown_pc()

    elif "restart computer" in command:
        speak("Restarting the computer")
        system.restart_pc()

    elif "lock" in command or "secure system" in command:
        speak("Locking the computer")
        system.lock_pc()

    elif "capture screen" in command:
        speak("Taking screenshot")
        result = system.take_screenshot()
        speak(result)

    elif "date" in command:
        today = datetime.date.today()
        speak(f"Today is {today}")

    elif "hello" in command:
        speak("Hello Faizan. How can I help you?")

    elif "system status" in command:
        result = system.system_status()
        speak(result)

    elif "internet speed" in command:
        result = system.internet_speed()
        speak(result)

    elif "battery status" in command:
        result = system.battery_status()
        speak(result)

    elif "roast me" in command:
        speak("You debug for three hours and the bug was a missing comma.")

    elif "focus mode" in command:
        speak("starting focus mode")
        system.open_app("code")

    elif "volume up" in command:
        speak(system.volume_up())

    elif "volume down" in command:
        speak(system.volume_down())

    elif "mute" in command:
        speak(system.mute_volume())

    elif "shutdown astra" in command:
        speak("Shutting down Astra")
        exit()

    else:
        speak("Command not recognized")