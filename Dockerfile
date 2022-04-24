FROM python:3.8.0
COPY . .
RUN apt update
RUN apt install ffmpeg libsm6 libxext6  -y
RUN python -m pip install -U pip
RUN pip install -r requirements.txt
RUN pip install -e .
CMD ["takslistwsb-app"]