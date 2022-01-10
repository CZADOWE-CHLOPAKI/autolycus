import subprocess

import cv2
from pydub import AudioSegment

from config import ProjectPaths, MAX_YOUTUBE_SHORT_LENGTH_MS
from utils import create_path_if_not_exists


def combine_sound(image_paths, start_meme_delay, end_meme_delay):
    # generate audio file and times of each meme
    audio_output = AudioSegment.silent(0)
    image_times_ms = []
    for path in image_paths:
        meme_audio = AudioSegment.silent(start_meme_delay)

        audio_path = path['root_path'] + '/audio.mp3'
        meme_audio += AudioSegment.from_mp3(audio_path)

        meme_audio += AudioSegment.silent(end_meme_delay)

        if len(meme_audio) + len(audio_output) >= MAX_YOUTUBE_SHORT_LENGTH_MS:
            break

        audio_output += meme_audio
        image_times_ms.append(len(meme_audio))

    return audio_output, image_times_ms


def assemble_video(image_paths):
    start_meme_delay = 100  # ms
    end_meme_delay = 1500  # ms

    resolution = (607, 1080)

    audio_output, image_times_ms = combine_sound(
        image_paths, start_meme_delay, end_meme_delay)

    audio_output.export(create_path_if_not_exists(
        ProjectPaths.COMBINED_SOUND), format="wav")

    img_array = []
    for path in image_paths[:len(image_times_ms)]:
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

    cmd = f'ffmpeg -hide_banner -loglevel error -y -i {ProjectPaths.VIDEO_NO_SOUND} -i {ProjectPaths.COMBINED_SOUND} -c:v copy -c:a aac {ProjectPaths.OUTPUT_VIDEO}'
    subprocess.call(cmd, shell=True)
    print('Assembling video done')
