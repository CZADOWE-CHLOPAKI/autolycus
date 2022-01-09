import cv2
import numpy as np
import glob
from pydub import AudioSegment
import subprocess


def combine_sound(image_paths, start_meme_delay, end_meme_delay):
    # generate audio file and times of each meme
    audio_output = 0
    image_times = []
    for path in image_paths:
        audio_output += AudioSegment.silent(start_meme_delay)

        audio_path = path['root_path'] + '/audio.mp3'
        fragment = AudioSegment.from_mp3(audio_path)
        audio_output += fragment

        audio_output += AudioSegment.silent(end_meme_delay)

        image_times.append(start_meme_delay+end_meme_delay + len(fragment))
    audio_output.export("audio.wav", format="wav")
    return audio_output, image_times


def assemble_video(image_paths):
    start_meme_delay = 100  # ms
    end_meme_delay = 1000  # ms

    resolution = (607, 1080)

    audio_output, image_times_ms = combine_sound(
        image_paths, start_meme_delay, end_meme_delay)

    img_array = []
    for path in image_paths:
        img = cv2.imread(path['file_path'])
        img = cv2.resize(img, resolution, interpolation=cv2.INTER_AREA)
        img_array.append(img)

    out = cv2.VideoWriter(
        'project.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, resolution)

    for image, image_time in zip(img_array, image_times_ms):
        for _ in range(image_time*30 // 1000):
            out.write(image)

    out.release()
    cmd = 'ffmpeg -y -i project.mp4 -i audio.wav -c:v copy -c:a aac output.mp4'
    subprocess.call(cmd, shell=True)
    print('Your memes are done my master1! UwU')
