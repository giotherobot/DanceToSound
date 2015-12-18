import pyaudio as pa
import numpy as np
import cv2
from matplotlib import pyplot as plt

CHUNK = 1024
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100


def note(freq, len, amp=1, rate=44100):
    t = np.linspace(0, len, len*rate)
    data = np.sin(2 * np.pi * freq * t)*amp

    return data.astype(np.int16)



p = pa.PyAudio()

tone = note(440, 2, amp=10000)

bytestream = tone.tobytes()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                output = True,
                frames_per_buffer = CHUNK)

stream.write(bytestream)


stream.stop_stream()
stream.close()
p.terminate()


