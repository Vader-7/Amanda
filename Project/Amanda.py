import speech_recognition as sr
import pyttsx3
import serial

listener = sr.Recognizer()
# arduino = serial.Serial("/dev/cu.usbmodem1301", 9600)
switch = 0
nose = []


def comandos(p_cadena):
    if "APAGAR" in p_cadena:
        SpeakText("ADIÓS, UN GUSTO")
        # arduino.write(p_cadena.encode("ascii"))
        return 1
    else:
        SpeakText(p_cadena)
        nose.append(p_cadena)
        # arduino.write(p_cadena.encode("ascii"))


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
            print("DIJISTE..." + cadena)
            switch = comandos(cadena)
        except:
            print("NO ENTENDI, REPITE LA PALABRA POR FAVOR.")

print(nose)
