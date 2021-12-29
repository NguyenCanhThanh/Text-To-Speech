from gtts import gTTS
import os
import playsound
import sys
import argparse

def speak(input, output, lang='en'):
    tts = gTTS(text=input, lang=lang)
    filename = output
    tts.save(filename)
    playsound.playsound(filename)
    # os.remove(filename)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Text to Speech gTTS")

    # Add the arguments to the parser
    ap.add_argument("-i", "--input", required=True,
                    help="input text")
    ap.add_argument("-o", "--output", required=True,
                    help="output voice")
    args = vars(ap.parse_args())
    # print("You passed: ", sys.argv)
    # ai_brain = "Xin chào Bạn."
    speak(args['input'], args['output'])
