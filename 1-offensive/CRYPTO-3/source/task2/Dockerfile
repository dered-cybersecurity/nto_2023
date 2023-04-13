FROM python:3.10-slim-buster
WORKDIR /app
RUN pip install flask pycryptodome
COPY . .
EXPOSE 1176
CMD ["python", "app.py"]