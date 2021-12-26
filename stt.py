#Python 2.x program to transcribe an Audio file
import speech_recognition as sr

AUDIO_FILE = ("example.wav")

# use the audio file as the audio source

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
	#reads the audio file. Here we use record instead of
	#listen
	audio = r.record(source)

try:
	print("The audio file contains: " + r.recognize_google(audio, language="uz-UZ"))

except sr.UnknownValueError:
	print("Speech Recognition could not understand audio")

except sr.RequestError as e:
	print("Could not request results from Speech Recognition service; {0}".format(e))
