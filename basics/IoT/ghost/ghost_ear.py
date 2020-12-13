import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    try:  
        with sr.Microphone() as source:
            print("ghost waiting")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("ghost listening")
            recorded_audio = recognizer.listen(source, timeout=3)
            print('ghost thinking')
    except:
        return 

    try:
        text = recognizer.recognize_google(
            recorded_audio,
            language="en-US"
        )
        return text
    except Exception as ex:
        print(ex)
        return
