import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

# use cwd to set root dir path
FILES_DIR = os.path.join(os.getcwd(), "data")

# change this
name_of_recording = "input.mp3"

# other folders
rec_src_dir = os.path.join(FILES_DIR, name_of_recording)

# get the file extension
file_ext = os.path.splitext(rec_src_dir)[1]

if file_ext == ".wav":
    # the file is already in WAV format
    audio = AudioSegment.from_wav(rec_src_dir)
else:
    # the file is in MP3 format, so we need to convert it to WAV
    audio = AudioSegment.from_file(rec_src_dir)
    output_file = os.path.splitext(rec_src_dir)[0] + ".wav"
    audio.export(output_file, format="wav")
    audio = AudioSegment.from_wav(output_file)

desired_sr = 22050

# define the minimum silence length (in milliseconds)
min_silence_len = 10000

# define the silence threshold (in decibels)
silence_thresh = -40

# split the audio into chunks of approximately 10 seconds
chunks = []
start_time = 0
end_time = 10000
while end_time <= len(audio):
    chunk = audio[start_time:end_time]
    chunks.append(chunk)
    start_time += 10000
    end_time += 10000