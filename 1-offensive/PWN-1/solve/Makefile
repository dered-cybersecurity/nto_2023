all: 
	@nasm -felf64 micro.asm && gcc -nostdlib -fstack-protector-all -no-pie -o micro micro.o
