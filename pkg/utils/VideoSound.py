import subprocess

import cv2
from pydub import AudioSegment

from pkg.config.config import MAX_YOUTUBE_SHORT_LENGTH_MS, ProjectPaths
from pkg.utils.utils import create_path_if_not_exists


class VideoSound:
    start_meme_delay = 100  # ms
    end_meme_delay = 1500  # ms

    def __init__(self, image_paths):
        self.image_paths = image_paths
        self.output_video_mp4_path = ProjectPaths.OUTPUT_VIDEO_MP4
        self.output_video_webm_path = ProjectPaths.OUTPUT_VIDEO_WEBM

        self.sound = Sound(ProjectPaths.COMBINED_SOUND)
        self.video_no_sound = VideoNoSound(ProjectPaths.VIDEO_NO_SOUND)

    def create_mp4(self):
        image_times_ms = self.sound.combine_sound(
            self.image_paths, self.start_meme_delay, self.end_meme_delay)
        self.sound.export_wav()

        self.video_no_sound.assemble_video(
            self.image_paths, image_times_ms)

        cmd = f'ffmpeg -hide_banner -loglevel error -y -i {self.video_no_sound.path()} -i {self.sound.path()} -c:v copy -c:a aac {self.output_video_mp4_path} '
        subprocess.call(cmd, shell=True)

    def convert_mp4_to_webm(self):
        cmd = f'ffmpeg -i {self.output_video_mp4_path} -c:v libvpx-vp9 -crf 30 -b:v 0 -b:a 128k -c:a libopus {self.output_video_webm_path}'
        subprocess.call(cmd, shell=True)


class VideoNoSound:
    def __init__(self, output_path):
        self.output_path = output_path

    def path(self):
        return self.output_path

    # FIXME in this function there is the bug thats corrupting video
    def assemble_video(self, image_paths, image_timestamps_ms):
        # construct resized array of images
        img_array = []
        resolution = (607, 1080)

        for path in image_paths[:len(image_timestamps_ms)]:
            img = cv2.imread(path['image_path'])
            img = cv2.resize(img, resolution, interpolation=cv2.INTER_AREA)
            img_array.append(img)

        image_timestamps_frames = [image_time_ms *
                                   0.03 for image_time_ms in image_timestamps_ms]

        # write video to path
        # https://stackoverflow.com/questions/30103077/what-is-the-codec-for-mp4-videos-in-python-opencv
        fps = 30
        videoWriter = cv2.VideoWriter(str(create_path_if_not_exists(
            self.output_path)), cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, resolution)

        for image, frames_per_image in zip(img_array, image_timestamps_frames):
            frames = 0
            while frames < frames_per_image:
                videoWriter.write(image)
                frames += 1

        videoWriter.release()


class Sound:
    def __init__(self, output_path):
        self.audio_output: AudioSegment = []
        self.output_path = output_path

    def path(self):
        return self.output_path

    def combine_sound(self, image_paths, start_meme_delay, end_meme_delay):
        # generate audio file and times of each meme
        self.audio_output = AudioSegment.silent(0)
        image_times_ms = []
        for path in image_paths:
            meme_audio = AudioSegment.silent(start_meme_delay)

            audio_path = path['root_path'] + '/audio.mp3'
            meme_audio += AudioSegment.from_mp3(audio_path)

            meme_audio += AudioSegment.silent(end_meme_delay)

            if len(meme_audio) + len(self.audio_output) >= MAX_YOUTUBE_SHORT_LENGTH_MS:
                break

            self.audio_output += meme_audio
            image_times_ms.append(len(meme_audio))

        return image_times_ms

    def export_wav(self):
        if self.audio_output == []:
            raise Exception("there is no audio in audio_output")

        self.audio_output.export(create_path_if_not_exists(
            self.output_path), format="wav")
