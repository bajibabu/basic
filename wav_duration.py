"""
This program computes the total duration of wave files.
It can take both single or multiple wavefiles as input.
Wave files should be in .wav format.
"""

import os
import sys


def wav_duration(wav_file):
    f = open(wav_file, 'r')
    # read the byterate from the file (see wav file format doc)
    # byterate is located at the first 28th byte
    f.seek(28)
    a = f.read(4)  # reads the 4 bytes from 28th position
    # convert string a into integer/longint value
    # a is little endian, so proper conversion is required
    byteRate = 0
    for i in range(4):
        byteRate = byteRate + ord(a[i])*pow(256, i)
    # get the file size in bytes
    fileSize = os.path.getsize(wav_file)  # get the file size in bytes
    # the duration of the data, in milliseconds, is given by
    ms = ((fileSize-44)*1000)/byteRate
    sec = ms/1000.  # this converts milliseconds to seconds
    f.close()
    return sec


def convert_time(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    time_str = "%i:%02i:%06.3f" % (hours, minutes, seconds)
    return time_str

if __name__ == "__main__":

    input_fd = sys.argv[1]  # it takes both file or directory as input
    duration = 0
    if os.path.isdir(input_fd):
        for file in os.listdir(input_fd):
	    (f, ext) = os.path.splitext(file)
            if ext != '.wav':
		continue
            wav_file = os.path.join(input_fd, file)
            duration = wav_duration(wav_file) + duration

    elif os.path.isfile(input_fd):
        duration = wav_duration(input_fd)

    else:
        sys.exit("Enter correct path/file..!")

    print "total duration is %s" % (convert_time(duration))
