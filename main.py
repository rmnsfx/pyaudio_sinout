from scipy.signal import butter, bilinear
import numpy as np
import time
import pyaudio
import math

# b, a = butter(3, 10000, fs=25600, btype='lowpass', analog=False)
# print(a, b, sep="\n")

# for i in range(p.get_device_count()):
#    dev = p.get_device_info_by_index(i)
#    print((i,dev['name'],dev['maxInputChannels']))


amplitude = 1
frequency = 100
sample_rate = 25600
length = 10  # sec.
time = np.arange(0, length, 1 / sample_rate)

samples = np.sin(2 * np.pi * frequency * time)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=sample_rate,
                frames_per_buffer=1024,
                output=True,
                output_device_index=2
                )

stream.write(samples.astype(np.float32).tobytes())
stream.close()
