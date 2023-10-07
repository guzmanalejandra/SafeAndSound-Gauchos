from PIL import Image 

input_image = Image.open("cons.jpg") 

pixel_map = input_image.load() 

width, height = input_image.size 

pixels = []

for i in range(width//2): 
	for j in range(height): 
		r, g, b= input_image.getpixel((i, j)) 
		pixels.append((r, g, b))



def convertPixelsArrayToNotes(pixels):
    notes = []
    for pixel in pixels:
        r, g, b = pixel
        if r == 0 and g == 0 and b == 0:
            notes.append("C")
        elif r == 0 and g == 0 and b == 255:
            notes.append("D")
        elif r == 0 and g == 255 and b == 0:
            notes.append("E")
        elif r == 0 and g == 255 and b == 255:
            notes.append("F")
        elif r == 255 and g == 0 and b == 0:
            notes.append("G")
        elif r == 255 and g == 0 and b == 255:
            notes.append("A")
        elif r == 255 and g == 255 and b == 0:
            notes.append("B")
        elif r == 255 and g == 255 and b == 255:
            notes.append("C")
    return notes