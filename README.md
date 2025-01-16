# MPU6050 wiring and sensor code I borrowed and modified (I also used code from the MPU 6050 library): 
https://www.youtube.com/watch?v=a37xWuNJsQI 

# Python Music Synthesis code that I borrowed from and modified: 
https://github.com/JamminCoder/music_maker 


Readme from music_maker:
# Rudimentary music maker/sound library with Python

#### Generating tone with pygame code taken and modified from: https://stackoverflow.com/a/16268034
#### Frequency map from: https://gist.github.com/sahithyen/b20922c902620e5bd6fd926263a93836


# Using the program:

First, install `pygame` and `numpy`. 
```
pip install pygame
```

```
pip install numpy
```

## Playing around with the library:

To play a note, you can use the `Note` class:
```python
from Note import Note
Note('C4').play() # Plays middle C for 1 second.

Note('E4', 3).play() # Plays E4 for 3 seconds
```

To play a chord, use the `play_chord()` method and pass in a list of `Note`s:

```python

# Plays a C major chord
Note.play_chord([
    Note('C4'),
    Note('E4'),
    Note('G4')
])
```

# The `Tone` class
Currently, the `Tone` class only generates sine waves.  
Here's how you do so:
```python
from play_tone import Tone

frequency = 440
duration = 1

# Plays a 440 Hz sine wave for 1 second.
Tone.sine(frequency, duration=duration)
```
