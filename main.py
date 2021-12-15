import speech_recognition as spreg
import pyttsx3 as txtsp
import webbrowser

recognizer = spreg.Recognizer()
ToTextEngine = txtsp.init()
ToTextEngine.say("Hi User, I am your Assistant")
ToTextEngine.say("What do I search today?")
ToTextEngine.runAndWait()

with spreg.Microphone() as mic:
        print("Hey there... I am listening....")
        voice = recognizer.listen(mic)
        voiceCommand = recognizer.recognize_google(voice)
        voiceCommand = voiceCommand.lower()
        # if 'listen' in voiceCommand:
        ToTextEngine.say(voiceCommand)
        ToTextEngine.runAndWait()
        print(voiceCommand)
        question = voiceCommand  # input question
        question = str(question).lower().replace("search for", '').replace("search", "")
        webbrowser.open('http://www.google.com/search?q=' + question)

