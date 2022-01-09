import requests


def download(image_url: str, file_name: str):
    r = requests.get(image_url)
    with open(file_name, 'wb') as f:
        f.write(r.content)
