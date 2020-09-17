import pyttsx3
"""
creates a pyttsk object that say some text at loud
"""
engine = pyttsx3.init()
engine.say("first time i'm using a package in next.py course")
engine.runAndWait()
