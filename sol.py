#!/usr/bin/env python3

from ctypes import CDLL
libc = CDLL("libc.so.6")
k = libc.time(0)
libc.srand(k)
#print("Current time is: %d" % k)
'print(libc.rand())'
w = libc.rand()

from pwn import *

io = process('sh')
#io.sendline('echo Hello World')
io = process('./time')
print(io.recvuntil(b'Enter your number: '))
io.sendline(b'%d' % w)
#result  = io.recvline()
#print(result)
print(io.recvall())
