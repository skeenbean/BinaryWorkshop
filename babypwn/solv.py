#!/usr/bin/env python

from pwn import *

p = process('babypwn')

gdb.attach(p, '''continue''')

p.interactive()
