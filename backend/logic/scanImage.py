from PIL import Image 
from logic.notas import notefreqs
import math





def getNote(original_number):
    
    Cscale = ["C","D","E","F","G","A","B"]
    
    
    
    normalized_number = original_number / maxValue
    notes = list(notefreqs.keys())
    
    # filter notes to the ones that are in the C scale
    notes = list(filter(lambda x: x[0] in Cscale, notes))
    
    # remove all the notes that have #
    notes = list(filter(lambda x: "#" not in x, notes))
    
    
    new_number = math.floor(normalized_number * (len(notes)-1))
    return notes[new_number]

def convertColorToRange(value,low=1,upper=100):
    return (value * (upper - low) / 255) + low
    


def convertPixelsArrayToNotes(pixels):
    notes = []
    global maxValue
    maxValue = 0
    for pixel in pixels:
        if pixel[0] > maxValue:
            maxValue = pixel[0]
        if pixel[1] > maxValue:
            maxValue = pixel[1]
        if pixel[2] > maxValue:
            maxValue = pixel[2]
    
    for pixel in pixels:
        # r - frequency
        # g - pitch
        # b - amplitude
        r, g, b = pixel
        note = getNote(r)
        note2 = getNote(g)
        note3 = getNote(b)
        # g = convertColorToRange(g, 1, 20)
        # b = convertColorToRange(b, 0.5,1.5)
        
        notes.append((note, note2, note3))
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

# image = Image.open('./logic/img3.jpg') 
# # resize image to 200x200
# image = image.resize((140,140))
# notes = getNotesFromImage(image)