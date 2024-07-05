from PIL import Image

def convert_to_grayscale(input_image_path, output_image_path):
    # Open the input image
    image = Image.open(input_image_path)
    
    # Convert the image to grayscale
    grayscale_image = image.convert("L")
    
    # Save the grayscale image
    grayscale_image.save(output_image_path)
    print(f"Grayscale image saved to {output_image_path}")

# Main program
if __name__ == "__main__":
    print("Image to Grayscale Converter")
    print("Type 'exit' to quit.")
    
    while True:
        # Get input from the user
        input_image_path = input("Enter the path to the input image: ")
        
        # Exit the program if the user types 'exit'
        if input_image_path.lower() == 'exit':
            break
        
        # Get the output path from the user
        output_image_path = input("Enter the path to save the grayscale image: ")
        
        # Convert the image to grayscale and save it
        convert_to_grayscale(input_image_path, output_image_path)
    
    print("Goodbye!")
