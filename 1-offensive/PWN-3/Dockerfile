
FROM phusion/baseimage:focal-1.2.0

ENV DEBIAN_FRONTEND noninteractive

RUN dpkg --add-architecture i386 && \
    apt-get -y update && \
    apt install -y \
    libc6:i386 \
    libc6-dbg:i386 \
    libc6-dbg \
    libffi-dev \
    libssl-dev \
    build-essential \
    netcat \
    socat \
    patchelf \
    tzdata --fix-missing && \
    rm -rf /var/lib/apt/list/*

run groupadd -r pwn && useradd -r -g pwn pwn

add build/libc.so.6 /home/pwn/lib/libc.so.6
add build/ld-2.31.so /home/pwn/lib/ld-2.31.so
add build/run.sh /home/pwn/.run.sh
add build/build.sh   /home/pwn/build.sh
add build/diary.c /home/pwn/diary.c
add build/launch.sh /home/pwn/launch.sh

run chmod 1733 /tmp /var/tmp /dev/shm
run chmod 555 /home/pwn/.run.sh
run chmod 555 /home/pwn/build.sh
run chmod 777 -R /home/pwn/lib
run chmod 555 /home/pwn/launch.sh

run bash -c "$(curl -fsSL https://gef.blah.cat/sh)"


workdir /home/pwn
add build/flag.txt flag.txt

run ./build.sh

run chmod 555 diary 
run chmod 444 flag.txt
run mv flag.txt flag-$(md5sum flag.txt | awk '{print $1}').txt

run rm diary.c
run rm build.sh

run chown -R root:pwn /home/pwn

run ls /home/pwn -lh

EXPOSE 2228 

entrypoint ["/home/pwn/.run.sh"]
