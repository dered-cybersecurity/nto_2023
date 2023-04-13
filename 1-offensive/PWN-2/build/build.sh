#!/bin/sh
gcc -Wl,--dynamic-linker=/glibc/2.27/64/lib/ld-2.27.so -Wl,--rpath=/glibc/2.27/64/lib notebook.c -o notebook -no-pie
