import os
import argparse
from pydub import AudioSegment

def convert_to_wav(mp3_folder, wav_folder):
    # create the output folder if it doesn't exist
    if not os.path.exists(wav_folder):
        os.makedirs(wav_folder)
    
    # loop through all the mp3 files in the folder
    for filename in os.listdir(mp3_folder):
        if filename.endswith('.mp3'):
            # load the mp3 file using pydub
            mp3_file = os.path.join(mp3_folder, filename)
            sound = AudioSegment.from_mp3(mp3_file)

            # create the output filename and save the file to the wav folder
            wav_file = os.path.join(wav_folder, os.path.splitext(filename)[0] + '.wav')
            sound.export(wav_file, format='wav')

if __name__ == '__main__':
    # set up command line arguments
    parser = argparse.ArgumentParser(description='Convert MP3 files to WAV format')
    parser.add_argument('mp3_folder', help='The folder containing the MP3 files')
    parser.add_argument('wav_folder', help='The folder where the WAV files should be saved')

    # parse the command line arguments
    args = parser.parse_args()

    # convert the files
    convert_to_wav(args.mp3_folder, args.wav_folder)
