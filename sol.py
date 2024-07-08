
from pwn import *

io = process('sh')
io.sendline('echo Hello World')
result  = io.recvline()
print(result)
