"""
This program normalizes the given wave files with total energy.
And also resampled to 16000 Hz sampling frequency.
Wave files should be in .wav format.
"""

import os
import sys
from scipy.io import wavfile
from scipy.signal import resample
import numpy as np

input_fd = sys.argv[1]

if os.path.isdir(input_fd):
    for file in os.listdir(input_fd):
	(f, ext) = os.path.splitext(file)
        if ext == '.wav':
            wav_file = os.path.join(input_fd, file)
	    fs, wav = wavfile.read(wav_file)
            # convert into float
            if wav.dtype == 'int16':
                wav = np.float32(wav)
                wav /= 32768
            # resample the file to 16000 Hz
            if fs != 16000:
                print wav_file, 'resampled into 16KHz'
                num = len(wav)*16000/fs
                print num
                fs = 16000
                wav = resample(wav, num=num)
            # computes the energy and normalize
            wav_eng = np.linalg.norm(wav)**2
            wav /= wav_eng
            # write the modified wav into a file
            wav /= 1.1*np.max(np.abs(wav))
            wav = np.int16(32768*wav)
            wavfile.write(filename=wav_file, rate=fs, data=wav)
else:
    sys.exit("Enter correct path/file..!")

