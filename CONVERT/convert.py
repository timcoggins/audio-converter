#import glob
import os
import fnmatch
import pydub
import sys
import shutil

#from scipy.io import wavfile as wav
#import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

os.system('clear')
print(bcolors.BOLD + '==========================================================')
print('SUPER AWESOME CONVERTER PROGRAM THAT IS SIMPLE YEAH YEAH')
print('==========================================================')
print('1: .WAV - 16bit / 44.1 kHz - Use this for Roland SPD SX')
print('2: .WAV - 16bit / 48 kHz')
print('3: .MP3 - 320kbps')
print('==========================================================')
chosen_format = raw_input(bcolors.ENDC + "Select format ")

print(chosen_format)
if chosen_format == '1':
    format_string = ' -acodec pcm_s16le -ar 44100 '
    extension = ".wav"
elif chosen_format == '2':
    format_string = ' -acodec pcm_s16le -ar 48000 '
    extension = ".wav"
elif chosen_format == '3':
    extension = ".mp3"
    format_string = ' -vn -ar 44100 -ac 2 -b:a 320k '
else:
    print('err.. are you ok?')
    sys.exit()

path = os.path.dirname(os.path.abspath(__file__))


clearout = raw_input(bcolors.HEADER + "CLEAR OUTPUT FOLDER? Type Y")

if clearout == 'y':
    for root, dirs, files in os.walk(path + '/OUT'):
        for f in files:
            os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))
        
        
             
        

fls = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in fnmatch.filter(files, '*.wav')]

x = 0
while x < len(fls):
    input_filename = fls[x]
    input_filename = input_filename.replace(' ', '\ ')
    output_filename = 'OUT/' + os.path.splitext(os.path.basename(fls[x]))[0] + extension
    output_filename = output_filename.replace(' ', '\ ')
    #print("ffmpeg -i " + input_filename + format_string + output_filename)
    os.system("ffmpeg -i " + input_filename  + format_string + output_filename)
    x = x + 1
    
print('==========================================================')
print('done master')
print(str(x) + ' files were converted')
print('==========================================================')

clearout = raw_input(bcolors.HEADER + "CLEAR INPUT FOLDER? Type Y")

if clearout == 'y':
    for root, dirs, files in os.walk(path + '/IN'):
        for f in files:
            os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))
        
        
