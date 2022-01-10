import os
import subprocess

import cv2
from pydub import AudioSegment

from config import ProjectPaths, YOUTUBE_SHORT_LENGTH
from src.utils import create_path_if_not_exists


def combine_sound(image_paths, start_meme_delay, end_meme_delay):
    # generate audio file and times of each meme
    audio_output = AudioSegment.silent(0)
    image_times = []
    for path in image_paths:
        audio_output += AudioSegment.silent(start_meme_delay)

        audio_path = path['root_path'] + '/audio.mp3'
        fragment = AudioSegment.from_mp3(audio_path)
        audio_output += fragment

        audio_output += AudioSegment.silent(end_meme_delay)
        # if len(audio_output_to_be_added) + len(audio_output) <= YOUTUBE_SHORT_LENGTH:
        #     audio_output += audio_output_to_be_added
        image_times.append(start_meme_delay + end_meme_delay + len(fragment))

    audio_output.export(create_path_if_not_exists(ProjectPaths.COMBINED_SOUND), format="wav")
    return audio_output, image_times


def assemble_video(image_paths):
    start_meme_delay = 100  # ms
    end_meme_delay = 1500  # ms

    resolution = (607, 1080)

    audio_output, image_times_ms = combine_sound(
        image_paths, start_meme_delay, end_meme_delay)

    img_array = []
    for path in image_paths:
        img = cv2.imread(path['file_path'])
        img = cv2.resize(img, resolution, interpolation=cv2.INTER_AREA)
        img_array.append(img)

    out = cv2.VideoWriter(
        str(create_path_if_not_exists(ProjectPaths.VIDEO_NO_SOUND)),
        cv2.VideoWriter_fourcc(*'mp4v'), 30, resolution)

    for image, image_time in zip(img_array, image_times_ms):
        for _ in range(image_time * 30 // 1000):
            out.write(image)

    out.release()

    # cmd  = 'ffmpeg -y -i audio.wav -filter:a "volume=1dB" audio2.wav'
    # subprocess.call(cmd, shell=True)

    # cmd = "ffmpeg -i CHINESE_RAP.mp3 -i audio.wav -filter_complex amix=inputs=2:duration=longest output4.mp3"
    # subprocess.call(cmd, shell=True)

    cmd = f'ffmpeg -y -i {ProjectPaths.VIDEO_NO_SOUND} -i {ProjectPaths.COMBINED_SOUND} -c:v copy -c:a aac {ProjectPaths.OUTPUT_VIDEO}'
    subprocess.call(cmd, shell=True)
    print('Assembling video done')
