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

COPY --from=skysider/glibc_builder64:2.27 /glibc/2.27/64 /glibc/2.27/64
COPY --from=skysider/glibc_builder32:2.27 /glibc/2.27/32 /glibc/2.27/32

run groupadd -r pwn && useradd -r -g pwn pwn

add build/run.sh /home/pwn/run.sh
add build/notebook.txt /home/pwn/notebook.txt
add build/build.sh   /home/pwn/build.sh
add build/notebook.c /home/pwn/notebook.c

run chmod 1733 /tmp /var/tmp /dev/shm
run chmod 555 /home/pwn/run.sh
run chmod 555 /home/pwn/build.sh


workdir /home/pwn
add build/flag.txt flag.txt

run ./build.sh

run chmod 555 notebook
run chmod 666 notebook.txt
run chmod 444 flag.txt
run mv flag.txt flag-$(md5sum flag.txt | awk '{print $1}').txt

run chown -R root:pwn /home/pwn

run ls /home/pwn -lh

EXPOSE 1337

entrypoint ["/home/pwn/run.sh"]
