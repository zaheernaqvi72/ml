import pyttsx3

engine = pyttsx3.init()
name = input("Enter your name: ")
engine.say(f"Hello {name}, How are you? I am your assistant. How can I help you? ")
engine.runAndWait()
engine.stop()