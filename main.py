from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys

recognizer = speech_recognition.Recognizer()
speaker = tts.init()
speaker.setProperty('rate', 150)

todo_list = ['Go Shopping', 'Record Song', 'Go Work']


def create_note():
    global recognizer

    speaker.say("What's your Note?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("Choose a filename!")
                speaker.runAndWait()

                filename = recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                filename = recognizer.listen(mic)

            with open(f"{filename}.txt", 'w') as f:
                f.write(note)

                done = True
                speaker.say(f"I successfully created the note!")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I didn't understand you. Please say again!")
            speaker.runAndWait()

def add_todo():
    global recognizer

    speaker.say("What to do do you want to add?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio)
                item= item.lower()

                todo_list.append(item)

                speaker.say(f"I added your Request in the list.")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand. Kinda say again!")
            speaker.runAndWait()


def show_todos():

    speaker.say("The items are as follows:")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()


def hello():
    speaker.say("Yeah! What can I do for you?")
    speaker.runAndWait()

def quit():
    speaker.say("GoodBye")
    speaker.runAndWait()
    sys.exit(0)


mappings = {
    "greeting": hello(),
    "create_note": create_note(),
    "add_todo": add_todo(),
    "show todos": show_todos(),
    "exit": quit()

}

assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()
while True:

    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio)
            message = message.lower()

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
