#!/bin/sh

while :; do
    socat -dd -T60 tcp-l:2228,reuseaddr,fork,keepalive,su=nobody exec:./launch.sh,stderr
done
