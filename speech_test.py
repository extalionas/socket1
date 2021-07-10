from gtts import gTTS
from playsound import playsound

audio = "speech.mp3"
language = 'ru'
example= input("enter текст\n")

sp = gTTS(text= example, lang = language,slow=False)

sp.save(audio)
playsound(audio)

