import numpy as np
from scipy import signal


def sinWave(frequency, duration, amplitude, samplingRate=44100):
    samples = np.sin(2 * np.pi * np.arange(samplingRate * duration) * frequency / samplingRate)
    samples = samples.astype(np.float32)    
    return samples*amplitude

def squareWave(frequency, duration, amplitude, samplingRate=44100):
    t = np.arange(samplingRate * duration)
    samples = signal.square(2 * np.pi * frequency * t)
    return samples * amplitude

def sawToothWave(frequency, duration, amplitude, samplingRate=44100):
    t = np.arange(samplingRate * duration)
    samples = signal.sawtooth(2 * np.pi * frequency * t / samplingRate)
    return samples * amplitude



    




