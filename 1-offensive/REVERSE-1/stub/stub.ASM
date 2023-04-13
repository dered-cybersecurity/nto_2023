format MZ
	push cs
	pop ds
	mov bx,hello
	mov cx, 32
	call print_flag
	
	symbol db '0','$'
	hello db 'This program cannot be run in DOS mode',24h
	db 03ah,01ch,00h,08h,048h,043h,01eh,03h,057h,02dh,0fh,05eh,057h,03ch,054h,0dh,06h,05fh,044h,04ch,03dh,03h,052h,042h,018h,031h,010h,05h,0ah,01h,065h,032h


print_flag:
    cx_pause dw 00001h
    cx_tmp dw 00000h
    mov cx,32
    mov si,hello
    mov di,symbol
next_symbol:
    mov WORD[cx_tmp],cx
    mov cx,WORD[cx_pause] ; ������� ����� ����� ����������� �����
    mov dx,0000h ; ������� ����� ����� ����������� �����
    mov ah,86h ; ������� 86h
    int 15h ; �����
    rol cx,1
    mov WORD[cx_pause],cx
    mov cx,WORD[cx_tmp]

    mov al,BYTE[si]
    mov ah, BYTE[si + 39]
    xor al, ah
    mov BYTE[di],al
    inc si
    mov ah,9
    mov dx,symbol
    int 21h

    loop next_symbol
    ret
	

