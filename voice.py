import speech_recognition as evren
import pyaudio

listener = evren.Recognizer()

try:
    with evren.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'evren' or "evrett" or "ev" in command:
            print(command)
except AttributeError or Exception as e:
    print(f"Encountered an error.. ({e})")
    pass