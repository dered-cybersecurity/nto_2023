from ubuntu:latest

run apt-get update && apt-get upgrade -y
run apt-get install socat -y
run groupadd -r pwn && useradd -r -g pwn pwn

add build/run.sh /home/pwn/run.sh
add chall/micro /home/pwn/chall

run chmod 1733 /tmp /var/tmp /dev/shm
run chmod 777 /home/pwn/run.sh

workdir /home/pwn
add build/flag.txt flag.txt

run chmod 777 chall
run chmod 444 flag.txt
run mv flag.txt flag-$(md5sum flag.txt | awk '{print $1}').txt

run chown -R root:pwn /home/pwn

run ls /home/pwn -lh

expose 8888

entrypoint ["./run.sh"]
