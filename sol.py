
from pwn import *

io = process(' sh ')
io.sendline(' echo Hello World ')
io.recvline()
