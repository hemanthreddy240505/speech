import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Please say something:")
    audio = r.listen(source)

    try:
        print("You said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand your audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
