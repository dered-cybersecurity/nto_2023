section .data
    msg db 'Oh wow, a buffer overflow, must be an easy task then..', 0xa, 0x0
    msgLen equ $ - msg


    global _start 

    section .text
_start:
    push rbp
    mov rbp, rsp
    lea rsi, msg
    mov rdx, msgLen
    mov rax, 1
    syscall

    lea rsi, [rbp - 0x20]
    xor rax, rax
    xor rdi, rdi
    xor r11, r11
    xor rcx, rcx
    mov rdx, 0x10000
    syscall
    ret
