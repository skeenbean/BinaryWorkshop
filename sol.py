
from pwn import *

io = process('./time')
print(io.recvuntil(b'Enter your number: '))
io.sendline(b'765690')
result  = io.recvline()
print(result)
