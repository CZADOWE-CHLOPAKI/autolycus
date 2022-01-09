import requests


def download(metadata):
    r = requests.get(metadata['url'])
    with open(metadata["file_name"]) as f:
        f.write(r.content)
