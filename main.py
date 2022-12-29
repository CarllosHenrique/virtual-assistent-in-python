import openai
import pyttsx3
from configs.voice import botVoz
from configs.gpt_config import gpt_informations
import speech_recognition as sr

while True:
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print('Ouvindo....')

		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		try:
			prompt = r.recognize_google(audio, language='pt-BR')
			print(': {}'.format(prompt))

			completion = gpt_informations(prompt)
			
			engine = botVoz()
	
			response = completion.choices[0].text

			print(response)

			engine.say(response)
			engine.runAndWait()

		except:
			print('WTF')



	

