#python program to remove image background
#type pip install rembg in the terminal to install the library
from rembg import remove
from PIL import Image
input_path='pl.jpg'
output_path='pl.png'
inp=Image.open(input_path)
output=remove(inp)
output.save(output_path)
