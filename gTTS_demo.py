from gtts import gTTS
from tempfile import NamedTemporaryFile
from playsound import playsound

tts = gTTS(text='Affirmative. Going to lab 300', lang='bn')
tts.save("synthesized.mp3")
playsound('synthesized.mp3')
