FROM python:3.10

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r /app/requirements.txt

COPY . .
CMD ["waitress-serve", "--host=0.0.0.0", "--port=3001", "--threads=4", "app:app"]
