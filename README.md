# luna_assistant

To start and use this script as a new user, follow these steps:

1. Install Required Libraries
    Ensure you have all the necessary Python libraries installed. Run the following commands in your terminal or command prompt:
        pip install SpeechRecognition pyttsx3 pywhatkit googletrans pillow.

2. Prepare Your Environment
    Python Version:
        Use Python 3.7 or later. Check your version by running:
        python --version
    GIF File:
        Place a GIF named Loading.gif in the same directory as your script. This GIF is used for the "Processing Command" animation.

3. Run the Script
    Save the script as a Python file, e.g., luna_assistant.py, and run it in your terminal or command prompt:
        python luna_assistant.py

4. Wake the Assistant
    After the animation and "Luna is ready" message:
        Speak a wake word like "Luna", "Hello", or "Hi Luna" or "okay Luna" or "Luna".
        The assistant will respond, "How can I assist you?".

5. Give Commands
    Once Luna is listening, you can say commands such as:
        "Open Google" – Opens Google in your web browser.
        "Open YouTube" – Opens YouTube.
        "File Manager" – Launches the file manager to select files.
        "Send WhatsApp" – (If implemented) Sends a WhatsApp message.
        "Open Notepad" – Opens system applications dynamically.
6. End the Program
    To stop Luna, say:
        "Stop", "Goodbye", or "Exit".
    Alternatively, press Ctrl + C in the terminal to terminate the script.



Common Issues and Fixes
    Microphone Not Working:
        Ensure your microphone is enabled and working.
        Test it using any other voice recording tool.

GIF File Missing:
    Ensure Loading.gif is in the same directory as the script.
    Replace the GIF with any valid GIF if needed.

Missing Dependencies:
    Re-run pip install to ensure all libraries are installed.

Background Noise:
    Run the assistant in a quiet environment to improve recognition accuracy.
