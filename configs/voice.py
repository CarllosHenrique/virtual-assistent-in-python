import pyttsx3

def botVoz():
    engine = pyttsx3.init()
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 100)

    volume = engine.getProperty('volume')
    engine.setProperty("volume",1)

    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[0].id)


    return engine