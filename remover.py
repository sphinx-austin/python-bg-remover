from rembg import remove
from PIL import Image


# path for inputing image file
input_path = " .jpg"

# output path
output_path = " .png"

#open the input image
#store it in the "inp" variable
inp = Image.open(input_path)

# passing the input image "inp" to remove the bg 
output = remove(inp)

# saving the output image with the background removed
output.save(output_path)

# background removed image
Image.open(".png")