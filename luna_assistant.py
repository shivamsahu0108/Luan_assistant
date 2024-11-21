import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import pywhatkit
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, filedialog
from openai import OpenAI
import threading
import time
from PIL import Image, ImageTk, ImageSequence


# Please Readme before the run.
# install the requirements # pip install -r requirements.txt
# Initialize speech engine
# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


# Set voice to female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use voices[0].id for male voice

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def show_command_animation():
    """Display an animation while processing a command."""
    def animate():
        try:
            gif = Image.open("Loading.gif")  # Ensure the GIF file exists in the same directory
            frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif)]
            frame_index = 0
            while not stop_animation.is_set():
                label.config(image=frames[frame_index])
                frame_index = (frame_index + 1) % len(frames)
                label.update_idletasks()
                time.sleep(0.1)
        except Exception as e:
            print(f"Animation error: {e}")

    root = tk.Tk()
    root.title("Processing Command")
    root.geometry("400x400")
    root.configure(bg="black")
    root.resizable(False, False)

    label = tk.Label(root, bg="black")
    label.pack(expand=True)

    threading.Thread(target=animate, daemon=True).start()

    def close_on_stop():
        if stop_animation.is_set():
            root.destroy()
        else:
            root.after(100, close_on_stop)

    close_on_stop()
    root.mainloop()

def search_google(query):
    """Search a query on Google."""
    webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")

def search_youtube(query):
    """Search a query on YouTube."""
    webbrowser.open(f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}")

def open_system_app(app_name):
    """Open a system application dynamically."""
    try:
        known_apps = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "paint": "mspaint.exe",
            "command prompt": "cmd.exe",
            "file explorer": "explorer.exe",
        }
        app_path = known_apps.get(app_name.lower())
        if app_path:
            os.startfile(app_path)
            speak(f"Opening {app_name}.")
        else:
            result = os.system(app_name.lower())
            if result != 0:
                speak(f"Could not open {app_name}. Please make sure it is installed.")
    except Exception as e:
        speak(f"Failed to open {app_name}. Error: {e}")

def open_file_manager():
    """Open the file manager and allow users to select a file or directory."""
    try:
        root = tk.Tk()
        root.withdraw()
        root.call('wm', 'attributes', '.', '-topmost', True)

        choice = filedialog.askopenfilename(title="Select a File to Open")
        if choice:
            os.startfile(choice)
            speak("Opening the selected file.")
        else:
            speak("No file was selected.")
    except Exception as e:
        speak(f"Error: {e}")

def send_whatsapp_message(number, message):
    """Send a WhatsApp message immediately."""
    try:
        pywhatkit.sendwhatmsg_instantly(number, message)
        speak("Message sent successfully.")
    except Exception as e:
        speak(f"Failed to send the message. Error: {e}")

# def aiProcess(command):
    client = OpenAI(api_key="<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>",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def process_command(command):
    """Process and execute the user's command."""
    stop_animation.clear()
    threading.Thread(target=show_command_animation, daemon=True).start()

    command = command.lower().strip()
    if command in ["stop", "exit", "goodbye"]:
        speak("Goodbye! Exiting.")
        stop_animation.set()
        exit(0)
    
    elif "search google for" in command:
        query = command.replace("search google for", "").strip()
        speak(f"Searching Google for {query}.")
        search_google(query)
    elif "search youtube for" in command:
        query = command.replace("search youtube for", "").strip()
        speak(f"Searching YouTube for {query}.")
        search_youtube(query)
    elif "open" in command:
        app_name = command.replace("open", "").strip()
        open_system_app(app_name)
    elif "file manager" in command or "file explorer" in command:
        open_file_manager()
    else:
        pass
        # # Let OpenAI handle the request
        # output = aiProcess(command)
        # speak(output) 

    stop_animation.set()

if __name__ == "__main__":
    recognizer = sr.Recognizer()

    try:
        stop_animation = threading.Event()

        speak("Luna is ready.")
        while True:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                try:
                    print("Listening for wake word...")
                    print("Say okay luna or Hi Luna...")
                    wake_word = recognizer.recognize_google(recognizer.listen(source))
                    if wake_word.lower() in ["hello", "hi luna", "luna", "okay luna"]:
                        speak("How can I assist you?")
                        with sr.Microphone() as source:
                            command = recognizer.recognize_google(recognizer.listen(source))
                            process_command(command)
                except sr.UnknownValueError:
                    continue
    except KeyboardInterrupt:
        speak("Exiting. Goodbye!")
    except Exception as e:
        speak(f"Error: {e}")
