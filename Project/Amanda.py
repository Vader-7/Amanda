import speech_recognition as sr
import pyttsx3
import serial

# Create a speech recognition object and a text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Create a dictionary to map commands to actions
commands = {
    "apagar": "exit",
    "hola": "greet",
    "cómo estás": "ask_how_are_you",
    "cómo te llamas": "ask_name",
    "qué haces": "ask_what_are_you",
    "qué es una lengua de señas": "explain_sign_language",
    "cuéntame un chiste": "tell_joke",
    "cuenta un chiste": "tell_joke",
    "cuál es tu color favorito": "ask_favorite_color"
}


# Define the actions for each command
def greet():
    engine.say("Hola, como estas?, mi nombre es Amanda")
    engine.runAndWait()


def ask_how_are_you():
    engine.say("Muy bien, gracias por preguntar")
    engine.runAndWait()


def ask_name():
    engine.say("Me llamo Amanda")
    engine.runAndWait()


def ask_what_are_you():
    engine.say("Soy un interprete de lengua de señas, y estoy aquí para ayudarte")
    engine.runAndWait()


def explain_sign_language():
    engine.say(
        "Una lengua de señas es un sistema de comunicación que utiliza la mano y los movimientos del cuerpo para expresar ideas, sentimientos y pensamientos")
    engine.runAndWait()


def tell_joke():
    engine.say("¿Qué le dice un pez a otro pez? .......nada")
    engine.runAndWait()


def ask_favorite_color():
    engine.say("Mi color favorito es el azul")
    engine.runAndWait()


# Define the main loop
while True:
    # Calibrate the speech recognition object to the ambient noise
    with sr.Microphone() as source:
        print("SILENCIO POR FAVOR, CALIBRANDO SONIDO DE FONDO.")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("CALIBRADO, HABLE AHORA......")

        # Listen for a command
        audio = recognizer.listen(source, phrase_time_limit=3)

        # Try to recognize the spoken command
        try:
            command = recognizer.recognize_google(audio, language='es-MX').lower()
            print("You said: " + command)

            # Check if the command is in the dictionary
            if command in commands:
                # Execute the action associated with the command
                action = commands[command]
                if action == "exit":
                    print("Goodbye!")
                    break
                else:
                    globals()[action]()
            else:
                # Send the command to the Arduino
                # arduino.write(command.encode("ascii"))
                print("Unrecognized command")
        except sr.UnknownValueError:
            print("Could not understand the command")
        except sr.RequestError as e:
            print("Error accessing the speech recognition service: {0}".format(e))
