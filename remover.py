from rembg import remove
from PIL import Image


# path for inputing image file
input_path = " .jpg"

# output path
output_path = " .png"

inp = Image.open(input_path)


ouput = remove(inp)