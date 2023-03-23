# Audio Artistry

import sys
import pyttsx3

# Initialize the text-to-speech engine
tts = pyttsx3.init()

# Print the title of the program
print('Text-to-Speech Program')
print('Enter text to speak, or "q" to quit.')

# Continuously prompt the user to enter text
while True:
    text = input('Enter text here: ')

    # Check if the user entered "q" to quit
    if text.lower() == 'q':
        sys.exit()  # Exit the program

    # Add the text for the tts engine to say
    tts.say(text)
    # Make the tts engine say the text
    tts.runAndWait()
