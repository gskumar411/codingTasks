Explanation:
Import the pyttsx3 Library:

The pyttsx3 library is imported to use its text-to-speech functionalities.
Initialize the Engine:

engine = pyttsx3.init() initializes the text-to-speech engine.
Function speak_text(text):

This function takes a string text as input and uses the engine to speak it.
engine.say(text) queues the text to be spoken.
engine.runAndWait() processes the voice command and waits for it to finish.
Main Program Loop:

The program runs an infinite loop, prompting the user to enter text.
If the user types 'exit', the loop breaks, and the program ends.
The input text is passed to the speak_text function to be spoken aloud.
Running the Program
Save the script to a file, for example, text_to_speech.py.
Run the script using Python:
Type any message into the prompt, and the program will speak it out loud.
To exit the program, type exit.
This simple program leverages the pyttsx3 library to make text-to-speech accessible and easy to use. Feel free to modify and expand upon it as needed!