import requests

def download(image):
    r = requests.get(image['url'])
    with open(image['fname'], 'wb') as f:
        f.write(r.content)
