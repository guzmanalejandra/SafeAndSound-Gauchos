from PIL import Image 
from notas import notefreqs

def getNote(original_number):
    normalized_number = original_number / 255
    new_number = round(normalized_number * 15)
    notes = list(notefreqs.keys())
    return notes[new_number]

def convertColorToRange(value,low=1,upper=100):
    return (value * (upper - low) / 255) + low
    


def convertPixelsArrayToNotes(pixels):
    notes = []
    for pixel in pixels:
        # r - frequency
        # g - pitch
        # b - amplitude
        r, g, b = pixel
        note = getNote(r)
        g = convertColorToRange(g, 1, 20)
        b = convertColorToRange(b, 0.5,1.5)
        notes.append((note, g, b))
    return notes

# tiene que recibir un objetoImgen de PIL
def getNotesFromImage(input_image):
    pixel_map = input_image.load() 
    width, height = input_image.size 
    pixels = []
    for i in range(width//2): 
        for j in range(height): 
            r, g, b= input_image.getpixel((i, j)) 
            pixels.append((r, g, b))

    all_notes = convertPixelsArrayToNotes(pixels)

    # separate notes in 3 arrays of the same size
    notes1 = all_notes[:len(all_notes)//3]
    notes2 = all_notes[len(all_notes)//3:2*len(all_notes)//3]
    notes3 = all_notes[2*len(all_notes)//3:]

    return [notes1, notes2, notes3]

image = Image.open('cons.jpg') 
notes = getNotesFromImage(image)