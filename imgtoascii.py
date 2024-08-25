from tkinter import Tk, filedialog
from PIL import Image
import os

# ASCII characters used for image conversion
ASCII_CHARS = "@%#*+=-:. "

# Function to resize the image while maintaining the aspect ratio
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width  # Calculate the aspect ratio
    new_height = int(new_width * ratio)  # Adjust the height to maintain aspect ratio
    resized_image = image.resize((new_width, new_height))  # Resize the image
    return resized_image

# Function to convert the image to grayscale
def grayscale_image(image):
    return image.convert("L")  # Convert the image to grayscale mode ("L")

# Function to map each pixel to an ASCII character
def pixels_to_ascii(image, scale=1):
    pixels = image.getdata()  # Get the pixel data from the image
    ascii_str = ""
    # Convert each pixel to an ASCII character based on its brightness
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value * (len(ASCII_CHARS) - 1) // 255]
    return ascii_str

def main():
    root = Tk()
    root.withdraw()  # Hide the Tkinter root window
    
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if not file_path:
        print("No file selected.")
        return
    
    # Try to open the selected image file
    try:
        image = Image.open(file_path)
    except Exception as e:
        print("Error:", e)
        return
    
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # Extract the image name without the extension
    image_name = os.path.splitext(os.path.basename(file_path))[0]
    # Define the output path for the ASCII art text file
    output_path = os.path.join(script_directory, f"{image_name}_ascii.txt")
    
    width = 200  # Set the desired width for the ASCII art

    # Resize the image and convert it to grayscale
    image = resize_image(image, width)
    image = grayscale_image(image)
    # Convert the grayscale image to an ASCII string
    ascii_str = pixels_to_ascii(image)
    
    img_height = image.size[1]  # Get the height of the resized image
    ascii_str_len = len(ascii_str)  # Get the length of the ASCII string
    # Split the ASCII string into lines based on the image width
    ascii_img = "\n".join([ascii_str[i:i+width] for i in range(0, ascii_str_len, width)])
    
    # Write the ASCII art to a text file
    with open(output_path, "w") as f:
        f.write(ascii_img)
    
    print("ASCII art saved to", output_path)  # Notify the user of the output location
    input()  # Wait for user input before closing the console

if __name__ == "__main__":
    main()
