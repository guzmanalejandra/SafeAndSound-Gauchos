import random
import logic.thinkdsp as thinkdsp
from pydub import AudioSegment
from pydub.playback import play
from logic.notas import notefreqs

randomCoeffs = []
for i in range(0,8):
    randomCoeffs.append(random.uniform(-1,1))
    
fourierCoeffs = {
    "sine":[0,1,0,0,0,0,0,0],
    "sawtooth":[0,0.6366,0,-0.2122,0,0.1273,0,-0.0909],
    "trumpet":[0.1155,0.3417,0.1789,0.1232,0.0678,0.0473,0.0260,0.0045,0.0020],
    "random":randomCoeffs   
}


def createNote(noteName="A4",octave=False,tipo="sine", amp=0.5, beats=1.0, filter=None, cutoff=None, filename="defaultFile"):
    # frequency = (notefreqs[noteName] * 2 ) if octave else notefreqs[noteName]
    frequency = notefreqs[noteName]
    duration = beats/2
    signal = thinkdsp.SinSignal(freq=0)
    
    # add harmonics
    for i in range(1,len(fourierCoeffs[tipo])):
        signal += thinkdsp.SinSignal(freq=frequency*i, amp=fourierCoeffs[tipo][i]*amp, offset=0)
        
    wave = signal.make_wave(duration=duration, start=0, framerate=44100)
    wave.write(filename+".wav")
    audio = AudioSegment.from_wav(filename+".wav")

    if filter == "lowpass":
        audio = audio.low_pass_filter(cutoff)
    elif filter == "highpass":
        audio = audio.high_pass_filter(cutoff)
    return audio

def createSpace(track,attack=100, release=100):
    for i in range(0,len(track)-1):
        if track[i][0:2]==track[i+1][0:2]:
            track[i]=track[i].fade_out(release)
            
def mix3Tracks(track1, track2, track3):
    createSpace(track1,50,50)
    createSpace(track2,50,50)
    createSpace(track3,50,50)
    
    song = AudioSegment.empty()
    
    for i in range(0,len(track1)):
        note1 = track1[i]
        note2 = track2[i]
        note3 = track3[i]
        song += note1[:len(note1)].overlay(note2[:len(note2)]).overlay(note3[:len(note3)])
    return song

# G3_long= createNote("G3", "sine", beats=2.0) 
# C4 = createNote("C4", "sine") 
# D4 = createNote("D4", "sine") 
# D4_long= createNote("D4", "sine", beats=2.0) 
# Eb4 = createNote("D#4", "sine") 
# E4 = createNote("E4", "sine") 
# F4_long= createNote("F4", "sine", beats=2.0) 
# Gb4 = createNote("F#4", "sine"); Gb4_long = createNote("F#4", "sine", beats=2.0)
# G4 = createNote("G4", "sine"); G4_long= createNote("G4", "sine", beats=2.0) 
# Ab4 = createNote("G#4" , "sine"); 
# A4 = createNote("A4", "sine"); A4_long= createNote("A4", "sine", beats=2.0) 
# B4 = createNote("B4", "sine"); B4_long= createNote("B4", "sine", beats=2.0) 
# C5 = createNote("C5", "sine") 
# D5 = createNote("D5", "sine"); D5_long= createNote("D5", "sine", beats=2.0) 
# G5_long= createNote("G5", "sine", beats=2.0) 
# # Song 1: Jingle Bells 
# trackl = [B4, B4, B4_long, B4, B4, B4_long, B4, D5, G4, A4, B4_long, B4_long, 

# C5, C5, C5, C5, C5, B4, B4, B4, B4, A4, A4, B4, A4_long, D5_long, 

# B4, B4, B4_long, B4, B4, B4_long, B4, D5, G4, A4, B4_long, B4_long, 

# C5, C5, C5, C5, C5, B4, B4, B4, D5, D5, C5, A4, G4_long, G5_long] 

# track2 = [G4, B4, D4_long, G4, B4, D4_long, G4, B4, D4, Gb4, G4_long, F4_long, 

# E4, G4, Eb4, G4, D4, G4, E4, Ab4, A4, E4, C4, E4, D4_long, Gb4_long, 

# G4, B4, D4_long, G4, B4, D4_long, G4, B4, D4, Gb4, G4_long, F4_long, 

# E4, G4, Eb4, G4, D4, G4, E4, Ab4, A4, E4, D4, Gb4, G4_long, G3_long ]

# songl = mix2Tracks(trackl, track2)


def procesarNotas(notes):
    widthImage = len(notes[0])
    cant = widthImage // 50
    print(widthImage)
    
    track1 = []
    track2 = []
    track3 = []
    
    # random boolean
    
    for i in range(0,widthImage,cant):
        randomBool = random.choice([True, False])
        randomSpeed = random.choice([0.5, 1])
        track1.append(createNote(notes[0][i][0],randomBool, "trumpet", beats=0.5))
        randomSpeed = random.choice([True, False])
        track2.append(createNote(notes[1][i][0],randomBool, "trumpet", beats=0.5))
        randomBool = random.choice([True, False])
        track3.append(createNote(notes[2][i][0],False, "sine", beats=0.5))
        
    
    song = mix3Tracks(track1, track2,track3)
    return song


# save as song.wav
# procesarNotas()
# A4_trumpet = createNote("A4", "trumpet", 1, 4)
# play(A4_trumpet)
