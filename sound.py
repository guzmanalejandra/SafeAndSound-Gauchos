import numpy as np
import sounddevice as sd
from main import notes
from notas import notefreqs
from scipy.signal import chirp

samplerate = 44100  
duration = 1  

def generate_bell_tone_with_scipy(note, pitch, amplitude):
    t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
    
    
    fundamental = chirp(t, f0=note, f1=note*2, t1=duration, method='quadratic')
    harmonic1 = 0.25 * chirp(t, f0=note*2, f1=note*4, t1=duration, method='quadratic')
    harmonic2 = 0.15 * chirp(t, f0=note*3, f1=note*6, t1=duration, method='quadratic')
    

    wave = fundamental + harmonic1 + harmonic2

    attack_time = 0.01
    decay_time = 0.2
    sustain_level = 0.1
    release_time = 0.7
    
    total_samples = len(t)
    attack_samples = int(attack_time * samplerate)
    decay_samples = int(decay_time * samplerate)
    release_samples = int(release_time * samplerate)
    sustain_samples = total_samples - attack_samples - decay_samples - release_samples
    
    attack_curve = np.linspace(0, 1, attack_samples)
    decay_curve = np.linspace(1, sustain_level, decay_samples)
    sustain_curve = np.full(sustain_samples, sustain_level)
    release_curve = np.linspace(sustain_level, 0, release_samples)
    
    envelope = np.concatenate([attack_curve, decay_curve, sustain_curve, release_curve])
    

    bell_wave = amplitude * wave * envelope
    
    return bell_wave

def create_bell_sound_from_notes_with_scipy(note_data, samplerate=44100):
    audio = np.array([])
    processed_notes = set()  
    for note_set in note_data:
        for note, pitch, amplitude in note_set:
            if note not in processed_notes:
                freq = notefreqs[note]
                tone = generate_bell_tone_with_scipy(freq, pitch, amplitude)
                audio = np.concatenate((audio, tone))
                print(f"Adding tone for note: {note}")
                processed_notes.add(note)
    
    return audio


sound_with_scipy = create_bell_sound_from_notes_with_scipy(notes)


sd.play(sound_with_scipy)


sd.wait()

print("Bell sound with scipy played successfully.")
