FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./api /code/api
COPY ./pkg /code/pkg
COPY ./secrets /code/secrets

ENV PYTHONPATH=./

CMD ["python", "api/main.py"]
