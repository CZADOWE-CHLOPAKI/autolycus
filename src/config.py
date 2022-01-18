from dataclasses import dataclass
from pathlib import Path

MAX_YOUTUBE_SHORT_LENGTH_MS = 60 * 1000
TEMP_ASSEMBLY_FILES_PATH = "./assemble_files/"
SECRETS_PATH = Path("./secrets")


@dataclass
class ProjectPaths:
    @dataclass
    class Root:
        OUTPUT = Path("output")
        OUTPUT_TEMP_FILES = OUTPUT / "temp"

    VIDEO_NO_SOUND = Root.OUTPUT_TEMP_FILES / "video_no_sound.mp4"
    COMBINED_SOUND = Root.OUTPUT_TEMP_FILES / "sound.wav"
    OUTPUT_VIDEO = Root.OUTPUT / "youtube_short.mp4"
