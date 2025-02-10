import speech_recognition as sr
from pydub import AudioSegment, silence
import os
import shutil

# use cwd to set root dir path
ROOT_DIR = os.path.join(os.getcwd(), "files")

# change this
name_of_recording = "training_voice_15min.mp3"

# other folders
rec_src_dir = f"{ROOT_DIR}/{name_of_recording}"
input_file = f"{ROOT_DIR}/wavs/{name_of_recording}"

