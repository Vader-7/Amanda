import speech_recognition as sr
import pyttsx3
import serial

listener = sr.Recognizer()
arduino = serial.Serial("/dev/cu.usbmodem1201", 9600)
switch = 0


def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


while switch != 1:
    with sr.Microphone() as source:
        print("SILENCIO POR FAVOR, CALIBRANDO SONIDO DE FONDO.")
        listener.adjust_for_ambient_noise(source, duration=2)
        print("CALIBRADO, HABLE AHORA......")
        try:
            audio = listener.listen(source, phrase_time_limit=3)
            cadena = listener.recognize_google(audio, language='es-MX')
            cadena = cadena.upper()
            if "APAGAR" in cadena:
                print("ADIÓS, UN GUSTO.")
                switch = 1
            else:
                arduino.write(cadena.encode("ascii"))
                print("DIJISTE.\t" + cadena)
        except:
            print("NO ENTENDI, REPITE LA PALABRA POR FAVOR.")
