import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pywhatkit
import os
import cv2

def listen_for_user():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Set the speed of speech
    engine.setProperty('voice', 'hindi')  # Set voice to Hindi

    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")  # Debugging message
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print(f"Recognized Command: {command}")  # Debugging output to see what is recognized
        if "hello jarvis" in command:
                engine.say("yes sir, myself jarvis . how may i help you ")
                engine.runAndWait()
                print("Waiting for instruction .....")
            
        elif "quit"  in command :
                engine.say("Good bye sir!, have a good day!")
                engine.runAndWait()
                return "stop"
        
        elif "access browser" in command:
                engine.say("Now you can access websites")
                engine.runAndWait()
                open_website(command)

        elif "date and time" in command:
                tell_time_and_date()

        
        elif "play song" in command :
                play_song_on_youtube()

        elif "power control" in command :
                system_control()

        elif "open camera" in command :
                camera_run()

    except sr.UnknownValueError:
        engine.say("Sorry, I couldn't understand. Can you please speak again")
        engine.runAndWait()
        print("speak again...")
        return False
    

            
def open_website(command):
    engine = pyttsx3.init()
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    engine.setProperty('rate', 150)  # Set the speed of speech
    engine.setProperty('voice', 'hindi')  # Set voice to Hindi

    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")  # Debugging message
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print(f"Recognized Command: {command}")  # Debugging output to see what is recognized

        if "open youtube" in command:
                engine.say("Opening YouTube now.")
                engine.runAndWait()
                webbrowser.open("https://www.youtube.com")
            
        elif "open gpt" in command:
                engine.say("Opening chatgpt now.")
                engine.runAndWait()
                webbrowser.open("https://www.chatgpt.com")
            
        elif "open google" in command:
                engine.say("Opening google now.")
                engine.runAndWait()
                webbrowser.open("https://www.google.com")
        

    except sr.UnknownValueError:
        engine.say("Sorry, I couldn't understand. Can you please speak again")
        engine.runAndWait()
        print("speak again...")
        return False

def tell_time_and_date():
    engine = pyttsx3.init()

    # Get current date and time
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")  # Get current time
    current_date = now.strftime("%A, %B %d, %Y")  # Get current date

    engine.say(f"The current time is {current_time} and today's date is {current_date}.")
    engine.runAndWait()

def play_song_on_youtube():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    engine = pyttsx3.init()

    try:
        with mic as source:
            engine.say("Which song would you like to play?")
            engine.runAndWait()
            print("Listening for song name...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            song_name = recognizer.recognize_google(audio).lower()
            print(f"Recognized Song: {song_name}")

        # Play song on YouTube
        engine.say(f"Playing {song_name} on YouTube.")
        engine.runAndWait()
        pywhatkit.playonyt(song_name)

    except sr.UnknownValueError:
        engine.say("Sorry, I couldn't understand the song name. Please try again.")
        engine.runAndWait()
    except Exception as e:
        engine.say("An error occurred while trying to play the song.")
        engine.runAndWait()
        print(f"Error: {e}")

def system_control():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    engine = pyttsx3.init()

    try:
        with mic as source:
            engine.say("Do you want to shut down or restart?")
            engine.runAndWait()
            print("Listening for system control command...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print(f"Recognized Command: {command}")

        if "shut down" in command:
            engine.say("Shutting down the system. Goodbye!")
            engine.runAndWait()
            os.system("shutdown /s /t 1")  # Shutdown command

        elif "restart" in command:
            engine.say("Restarting the system. Please wait!")
            engine.runAndWait()
            os.system("shutdown /r /t 1")  # Restart command

        else:
            engine.say("I didn't understand the command. Please say shut down or restart.")
            engine.runAndWait()

    except sr.UnknownValueError:
        engine.say("Sorry, I couldn't understand your command. Please try again.")
        engine.runAndWait()
    except Exception as e:
        engine.say("An error occurred while trying to execute the command.")
        engine.runAndWait()
        print(f"Error: {e}")

def camera_run():
    cap = cv2.VideoCapture(0)
    engine = pyttsx3
    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Cannot access the camera.")
        return

    print("Press 'q' to quit.")
    

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If the frame is read correctly, ret is True
        if not ret:
            print("Error: Cannot read frame.")
            break

        # Display the frame
        cv2.imshow('Camera Feed', frame)

        # Ensure 'q' works for quit
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()




if __name__ == "__main__":
    while True:
        result = listen_for_user()
        if result == "stop":  # Exit the loop if "stop" is recognized
            print("Bye! see u soon ")
            break  # Exit the loop when "stop" is said
