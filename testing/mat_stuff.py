import sys
from PySide import QtGui
from scipy.io import wavfile
import numpy as np
import scipy.fftpack as fftpack

import matplotlib.pyplot as plt

class SoundData:
    def loadData(self, fname):
        self.rate, self.data = wavfile.read(fname)
        if (len(data.T) > 1):
            self.data = self.data.T[0]

    def fft(data, intervalSize, rangeofFreq):
        if (len(data) < intervalSize):
            return None;
        start = np.random.randint(0, len(data) - intervalSize + 1)
        chunked = data[start:(start + intervalSize)]
        interv = (start, start + intervalSize)
        return fftpack.fft(chunked, rangeofFreq), interv


    # freq, data = loadData('1.wav')
    # sample_rate = 20000


    def toRealFreq(f):
        return round(f * (freq / sample_rate))


    def toDFTFreq(f):
        return round(f * (sample_rate / freq))


    data = np.divide(data, max(data))

    print(freq)
    print(len(data))
    result, randInterval = fft(data, freq // 2, sample_rate)
    print(freq // 2)

    magnitudes = [np.absolute for y in result[0:len(result) // 2]]
    phase = [np.angle for y in result[0:len(result) // 2]]

    print(magnitudes.index(max(magnitudes)))
    print(len(magnitudes))

    plt.figure(figsize=(20, 10))
    plt.xscale('log');
    plt.yscale('log');
    plt.title("Frequency Graph of Song");
    plt.plot(magnitudes)
    plt.show()