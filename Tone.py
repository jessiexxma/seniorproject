import math
from os import stat
import numpy
import time
import pygame
import threading

pygame.init()
bits = 16
sample_rate = 44100
pygame.mixer.pre_init(sample_rate, bits)

def sine_x(amp, freq, time):
    return int(round(amp * math.sin(2 * math.pi * freq * time))) #generating sine waves

class Tone:

    @staticmethod
    def fade_in_out(length, sample_rate):
        fade_length = int(0.05 * sample_rate)  # 5ms fade in/out to remove clicky sound
        fade_in = numpy.linspace(0, 1, fade_length)
        fade_out = numpy.linspace(1, 0, fade_length)
        fade = numpy.concatenate((fade_in, numpy.ones(length - 2 * fade_length), fade_out))
        return fade
    
    def sine(frequency, duration=1, speaker=None, volume=1.0): #def sine(frequency, duration=1, speaker=None): #
        """
        Play tone code taken and modified from https://stackoverflow.com/a/16268034
        """

        num_samples = int(round(duration * sample_rate))

        buf = numpy.zeros((num_samples, 2), dtype = numpy.int16)
        amplitude = (2 ** (bits - 1) - 1 ) * volume #increasing amplitude = increasing volume
        fade = Tone.fade_in_out(num_samples, sample_rate) #fade helps make the bumpy noise thing not happen

        for s in range(num_samples):
            t = float(s) / sample_rate    # time in seconds

            sine = sine_x(amplitude, frequency, t) * fade[s]
            
            # Control which speaker to play the sound from
            if speaker == 'r':
                buf[s][1] = sine # right
            elif speaker == 'l':
                buf[s][0] = sine # left

            else:
                buf[s][0] = sine # left
                buf[s][1] = sine # right
                

        sound = pygame.sndarray.make_sound(buf)
        one_sec = 1000 # Milliseconds
        sound.play(loops = 1, maxtime=int(duration * one_sec))
        time.sleep(duration)
    
    @staticmethod
    def create_tone_from_list(frequency_array, duration=1):
        tone_threads = []
        
        for freq in frequency_array:
            thread = threading.Thread(target=Tone.sine, args=[freq, duration])
            tone_threads.append(thread)
        
        for thread in tone_threads:
            thread.start()
        
        for thread in tone_threads:
            thread.join()




