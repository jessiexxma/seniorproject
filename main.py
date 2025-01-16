import serial
from Note import Note
from Tone import Tone
import time
import numpy as np
from scipy.signal import butter, lfilter, filtfilt
from scipy.signal import freqs
import scipy.signal as signal

#---Connecting I2C and serial communication with arduino---
serialInst = serial.Serial()
serialInst.baudrate = 9600
#   ports: 
#   "/dev/cu.HC-05"
#   "/dev/cu.usbmodem101"
serialInst.port = "/dev/cu.usbmodem101"
serialInst.open()


#attempt at low-pass filter - did not work. 
def low_pass_filter(data, cutoff_freq=6000, fs=44100, order=2): #data, cuttoff_frequency, fs = sample rate Hz - taken from tone, order = sine wave quadratic order?
    nyquist_freq = 0.5 * fs #nyquist frequency
    normal_cutoff = cutoff_freq / nyquist_freq
    
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    
    filtered_data = lfilter(b, a, data)

    print(filtered_data) 
    return filtered_data

def read_data():
    if serialInst.in_waiting:
        sequence = serialInst.readline().decode("utf").strip().split() #reads serial monitor and decodes data
        if len(sequence) == 6:
            ax, ay, az, gx, gy, gz = sequence #splits into sequence

            return [int(ax), int(ay), int(az), int(gx), int(gy), int(gz)]
        else:
            print("not correct # of sequence")

def processing_data_music():
    try:
        sequence = read_data()
        print(sequence)
       
        # mapped_gyro = abs(sequence[3] - 100) * 100 #converts gyroscope data to change noise
        # # if mapped_gyro > 4000:
        # #     mapped_gyro = 4000
        mapped_gyro = sequence[3] * 10 #converts gyroscope data to change noise
        # if mapped_gyro > 4000:
        #     mapped_gyro = 4000

        mapped_accel = sequence[2]/255 #converts accelerometer data to volume, to be between 0 and 1
        if mapped_accel > 1:
            mapped_accel = 1
        
        #actually playing the note
        Note(mapped_gyro, duration=0.1, volume=mapped_accel).play()

    except Exception as e:
        print("Exception:", e)
        time.sleep(1)




while True:
    processing_data_music()


''' #attempt at using filter
def processing_data_music():
    try:
        sequence = read_data()
        print(sequence)
       
        filtered_gyro = low_pass_filter(sequence[3])
        mapped_gyro = abs(filtered_gyro - 128) * 80 #converts gyroscope data to change noise
        if mapped_gyro > 4000:
            mapped_gyro = 4000

        filtered_accel = low_pass_filter(sequence[2])
        mapped_accel = filtered_accel/255 #converts accelerometer data to volume, to be between 0 and 1
        if mapped_accel > 1:
            mapped_accel = 1
        
        #actually playing the note
        Note(mapped_gyro, duration=0.1, volume=mapped_accel).play()
    except Exception as e:
        print("Exception:", e)
        time.sleep(1)
        '''


