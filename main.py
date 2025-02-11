import speech_recognition as sr
from pydub import AudioSegment, silence
import os

# use cwd to set root dir path
FILES_DIR = os.path.join(os.getcwd(), "files")

# change this
name_of_recording = "training_voice_15min.mp3"

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