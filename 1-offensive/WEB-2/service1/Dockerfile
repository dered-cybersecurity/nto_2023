FROM python:3.10

WORKDIR /app

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "waitress-serve", "--host=0.0.0.0", "--port=3000", "--threads=4", "app:app"]
