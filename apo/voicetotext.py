import speech_recognition as sr 
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
	audio = r.adjust_for_ambient_noise(source, duration =6)
	audio = r.listen(source, timeout = 6)
try:
	result = r.recognize_google(audio)
	print(result)
except LookupError:
	print("could not understand")