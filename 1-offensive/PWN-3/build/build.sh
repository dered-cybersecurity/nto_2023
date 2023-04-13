#!/bin/sh

gcc -Wl,--dynamic-linker=/home/pwn/lib/ld-2.31.so -Wl,--rpath=/home/pwn/lib/ -no-pie -fno-stack-protector diary.c -o diary
patchelf --set-interpreter /home/pwn/lib/ld-2.31.so --set-rpath /home/pwn/lib diary
