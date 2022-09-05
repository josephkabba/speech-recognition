import pyttsx3, time 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice.id)  # changes the voice
    engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()