import pyttsx3
import re
import stackapi
import speech_recognition as sr
from stackapi import StackAPI 

def listentomic():
	try:
		with mic as source:
			print("listening..")
			audio = r.adjust_for_ambient_noise(source, duration =2)
			audio = r.listen(source, timeout = 2)
			result = r.recognize_google(audio)
			print(result)
	except LookupError:
		print("could not understand")
	return result



def jira(command):
	pass

def confluence(command):
	pass

def bitbucket(command):
	pass
	

def stackoverflow(command):
	try:
		site = StackAPI('stackoverflow')
		engine.say("tell id of question")
		engine.runAndWait()
		id = listentomic()
		#id = input("enter id of question:")
		question = site.fetch('questions/%s'%(id))
		print(question)
		engine.say("what do you want from this question")
		engine.runAndWait()
		req = listentomic()
		#req = input("what do you want from this question:")
		if req == 'wrong':
			stackoverflow(command)
		else:	
			engine.say("the %s for this question is"%req)
			engine.runAndWait()
			print(question["items"][0][req])


	except stackapi.StackAPIError as e:
		print("   Error URL: {}".format(e.url))
		print("   Error Code: {}".format(e.code))		
		print("   Error Error: {}".format(e.error))
		print("   Error Message: {}".format(e.message))		

if __name__ == "__main__":
	r = sr.Recognizer()
	mic = sr.Microphone()
	engine = pyttsx3.init()
	engine.setProperty('rate',175)
	engine.say("hello, please tell your name.")
	engine.runAndWait()
	name = listentomic()
	#name = input("enter your name:")
	engine.say("hello %s, what can i do for you."%name)
	engine.runAndWait()
	command = listentomic()
	#command = input()

	if re.search('jira', command):
		jira(command)
	elif re.search('confluence', command):
		confluence(command)
	elif re.search('bitbucket', command):
		bitbucket(command)
	elif re.search('stack', command):
		stackoverflow(command)	 		
	else:
		print("sorry")	
	
	