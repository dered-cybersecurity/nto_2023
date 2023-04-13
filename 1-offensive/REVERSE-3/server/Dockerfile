FROM phusion/baseimage:focal-1.2.0

ENV DEBIAN_FRONTEND noninteractive

ENV TZ Europe/Moscow

RUN dpkg --add-architecture i386 && \
    apt-get -y update

RUN apt install -y python3 python3-pip 

RUN ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata
    
RUN python3 -m pip install -U pip

WORKDIR /app/
COPY player.py /app/
COPY rooms.py /app/
COPY server.py /app/
COPY graph.py /app/
COPY check /app/

ENTRYPOINT ["python3","-u","/app/server.py", "--tcpport", "1337","--capacity", "5"]
