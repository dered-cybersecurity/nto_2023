FROM ubuntu:22.04

ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && apt install -y npm
RUN npm install -g yarn

RUN mkdir /app

COPY app/package.json /app
COPY app/yarn.lock /app

WORKDIR /app

RUN yarn

COPY app /app

COPY flag.txt /

RUN chmod +x start.sh

EXPOSE 8080

ENTRYPOINT /bin/sh /app/start.sh
