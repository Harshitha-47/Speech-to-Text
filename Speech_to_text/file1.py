import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

# This function is used to allow the user to record their own text and it allows the user to access the microphone
# After taking the audio input, it will convert the audio into the string format
def record_text():
    while(1):
        try:
            # Use the microphone as source for input
            with sr.Microphone() as source2:
                # Prepare recognizer to receive input from the microphone
                r.adjust_for_ambient_noise(source2, duration=0.2)
                # Listens for the user's input
                audio2 = r.listen(source2)
                # Recognize speech using Google Speech Recognition
                MyText = r.recognize_google(audio2)

                return MyText

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Could not understand the audio")

# This function takes the string from the record_text function and outputs it to a text file
# HENCE THE SPEECH TO TEXT HAS BEEN COMPLETED FROM THE TWO FUNCTIONS GIVEN HERE
def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text = record_text()
    output_text(text)
    print("Wrote text")