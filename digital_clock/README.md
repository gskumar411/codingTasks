Explanation:
Import Libraries:

tkinter is used for creating the GUI.
strftime from the time module is used to get the current time in a formatted string.
Function time():

This function fetches the current time and updates the label text.
It uses after(1000, time) to call itself after 1000 milliseconds (1 second) to update the time continuously.
Main Application Window:

root = tk.Tk() initializes the main window.
root.title("Digital Clock") sets the window title.
Label Configuration:

label = tk.Label(...) creates a label with specific font, background, and foreground colors.
label.pack(anchor='center') centers the label in the window.
Start the Time Update:

time() is called once to initiate the first time update.
root.mainloop() starts the Tkinter event loop, which keeps the application running.
You can run this script in any Python environment that supports tkinter. The clock will display in a window with a purple background and white text, updating every second.