from PIL import Image
import os

# Specify the input folder containing PNG files
input_folder = 'input'

# Specify the output folder where JPG files will be saved
output_folder = 'output'

# Ensure the output folder exists, create it if it doesn't
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List all files in the input folder
input_files = os.listdir(input_folder)

# Iterate through the files in the input folder
for filename in input_files:
    if filename.endswith('.png'):
        # Construct the full file paths for input and output
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpg')

        # Open the PNG image and convert it to JPG
        img = Image.open(input_path)
        img.convert('RGB').save(output_path, 'JPEG')
        print(f'Converted {filename} to {os.path.basename(output_path)}')

print("Conversion complete.")
