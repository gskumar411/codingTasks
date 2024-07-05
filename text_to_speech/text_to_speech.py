import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Function to speak the given text
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Main program
if __name__ == "__main__":
    print("Text-to-Speech Talker")
    print("Type 'exit' to quit.")
    
    while True:
        # Get input from the user
        user_input = input("Enter the text you want to hear: ")
        
        # Exit the program if the user types 'exit'
        if user_input.lower() == 'exit':
            break
        
        # Speak the input text
        speak_text(user_input)
    
    print("Goodbye!")
