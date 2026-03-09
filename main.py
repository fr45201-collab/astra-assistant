from voice import speak, listen
from commands import handler

WAKE_WORD = "astra"

speak("Astra online. How may I assist you, Faizan?")

while True:

    mode = input("\nVoice (v) or Terminal (t): ").lower()

    # -------- VOICE MODE --------
    if mode == "v":

        command = listen()

        if not command:
            continue

        command = command.lower()

        # Wake word detection
        if any(word in command for word in ["astra", "astro", "hey astra"]):

            speak("Yes Faizan")

            for word in ["astra", "astro", "hey astra"]:
                command = command.replace(word, "")
                
                command = command.strip()

            if command:
                handler(command)

        else:
            print("Wake word not detected.")

    # -------- TERMINAL MODE --------
    elif mode == "t":

        command = input("You: ").lower()

        handler(command)

    else:
        print("Invalid mode. Choose 'v' or 't'.")