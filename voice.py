import speech_recognition as s
import pyaudio
import pyttsx3

listener = s.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('')

def talk(text):
    engine.say(text)
    # engine.say('How can I help you?')
    engine.runAndWait()

def take_command():
    try:
        with s.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            # if 'alexa' in command:
            #     # talk(command)
    except AttributeError or Exception as e:
        print(f"Encountered an error.. ({e})")
        pass
    return command

def play_song(command):
    song = command.replace('play', '')
    song2 = command.rsplit('play', 2)
    talk('playing' + song2[1])
    print(song)
    print(song2[1])


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        play_song(command)

run_alexa()

