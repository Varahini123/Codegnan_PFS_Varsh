'''
import pyttsx3
engine = pyttsx3.init()
name = "hayma"
def speak_in_text(text):
    engine.say(text)
    engine.runAndWait()
print("hi this is",name)
speak_in_text("hello{name},I'm AI,your new voice assistant")


import pyttsx3
engine = pyttsx3.init()
def speak_in_text(text):
    engine.say(text)
speak_in_text("hello,I'm AI,your new voice assistant")
speak_in_text("what's your plan today")
engine.runAndWait()
'''

import pyttsx3
engine=pyttsx3.init()
def speech_text(text):
    engine.say(text)
user_text=input("enter your message: ").lower()
name = "user"
if"my name is" in user_text:
    name = user_text.split("my name is")[-1].strip()
elif "name is" in user_text:
    name=user_text.split("name is")[-1].strip()
if user_text in["hi","hello","hey"]:
    response="Hello!How can i help you?"
elif "name" in user_text:
    response=f"Hello{name},How can i help you?"
else:
    response="sorry,i didn't get that"
print(response)
speech_text(response)
engine.runAndWait()
































