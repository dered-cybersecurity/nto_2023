#!/usr/bin/env sh

BINARY=/home/pwn/chall
PORT=8888

while :; do
    socat -dd -T60 tcp-l:$PORT,reuseaddr,fork,keepalive,su=nobody exec:$BINARY,stderr
done
