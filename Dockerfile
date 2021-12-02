FROM python:3.9-buster

WORKDIR /project
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT} dashboard:app"]