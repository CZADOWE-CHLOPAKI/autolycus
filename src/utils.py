from pathlib import Path

import requests


def download(image_url: str, file_name: str):
    r = requests.get(image_url)
    with open(file_name, 'wb') as f:
        f.write(r.content)


def create_path_if_not_exists(path: Path) -> Path:
    """
    Takes path to some file, creates necessary directories and returns given path
    :param path: path to some file
    :return: path
    """
    if not path.exists():
        path.parents[0].mkdir(exist_ok=True, parents=True)
    return path
