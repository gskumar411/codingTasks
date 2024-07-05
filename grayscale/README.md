Explanation:
Import the Image Class from PIL:

The Image class from the Pillow library is imported to handle image operations.
Function convert_to_grayscale(input_image_path, output_image_path):

This function takes the input image path and output image path as arguments.
Image.open(input_image_path) opens the input image.
image.convert("L") converts the image to grayscale. The "L" mode means luminance (grayscale).
grayscale_image.save(output_image_path) saves the grayscale image to the specified output path.
Main Program Loop:

The program runs an infinite loop, prompting the user to enter the path to the input image and the path to save the output image.
If the user types 'exit', the loop breaks, and the program ends.
The convert_to_grayscale function is called with the provided paths to perform the conversion and save the result.
Running the Program
Save the script to a file, for example, image_to_grayscale.py.
Run the script using Python
Enter the path to the image you want to convert when prompted, and then enter the path where you want to save the grayscale image.
To exit the program, type exit.
This program demonstrates how to use the Pillow library to perform a simple image manipulation task. Feel free to modify and expand upon it as needed!