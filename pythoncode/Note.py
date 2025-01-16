from importlib.resources import is_resource
#from utils import NOTE_MAP
from Tone import Tone
import threading
import time


class Note:
    def __init__(self, note, duration=1, volume=1.0): #initiates note
        self.duration = duration
        self.volume = volume
        if note == 'rest': #checks if note is resting
            self.is_resting = True
            return
        else:
            self.is_resting = False

        self.frequency = note
        
        
    
    def play(self, speaker=None, volume=1.0):
        if not self.is_resting:
            Tone.sine(self.frequency, duration=self.duration, speaker=speaker, volume=self.volume) #calls tone - plays tone
        else:
            time.sleep(self.duration)

    @staticmethod
    def rest(duration):
        return Note('rest', duration)

    @staticmethod
    def play_chord(notes):
        threads = []
        for note in notes:
            thread = threading.Thread(target=note.play)
            threads.append(thread)
        
        for thread in threads:
            thread.start()
        
        for thread in threads:
            thread.join()
        
