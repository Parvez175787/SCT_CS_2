import numpy as np
from PIL import Image

def load_image(image_path):
    img = Image.open(image_path)
    return np.array(img)

def save_image(image_array, output_path):
    img = Image.fromarray(image_array)
    img.save(output_path)

def swap_pixels(image_array):
    # Swap pixels in the image
    shuffled_image = image_array.copy()
    np.random.shuffle(shuffled_image)
    return shuffled_image

def apply_math_operation(image_array, operation):
    # Apply a basic mathematical operation to each pixel
    if operation == "invert":
        return 255 - image_array
    elif operation == "add":
        return np.clip(image_array + 50, 0, 255)
    elif operation == "subtract":
        return np.clip(image_array - 50, 0, 255)
    else:
        raise ValueError("Unsupported operation")

def encrypt_image(image_path, output_path, operation):
    image_array = load_image(image_path)
    
    if operation == "swap":
        encrypted_image = swap_pixels(image_array)
    else:
        encrypted_image = apply_math_operation(image_array, operation)
    
    save_image(encrypted_image, output_path)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Simple Image Encryption Tool")
    parser.add_argument("image_path", type=str, help="Path to the input image")
    parser.add_argument("output_path", type=str, help="Path to save the encrypted image")
    parser.add_argument("operation", type=str, choices=["swap", "invert", "add", "subtract"], help="Encryption operation to apply")
    
    args = parser.parse_args()
    
    encrypt_image(args.image_path, args.output_path, args.operation)
