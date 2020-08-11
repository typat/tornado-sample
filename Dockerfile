FROM python:3.7.6-slim-stretch

# Keep requirements and pip install separate so that this layer is cached separately from the other files below
COPY requirements.txt /
COPY sample.py settings.py /
COPY handlers /handlers
COPY templates /templates
COPY static /static

RUN python3 -m pip install -r /requirements.txt

EXPOSE 8080

CMD ["python", "./sample.py"]
