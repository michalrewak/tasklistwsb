FROM python:latest
EXPOSE 80
WORKDIR /usr/app

COPY ./ ./

RUN python -m venv env
RUN pip install -r requirements.txt

CMD ["python","app.py"]
