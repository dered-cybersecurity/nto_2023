#!/bin/sh


while :; do
    socat -dd -T60 tcp-l:1337,reuseaddr,fork,keepalive,su=nobody exec:/home/pwn/notebook,stderr
done
