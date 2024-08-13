# 'time' Challenge Solution

## details the steps taken to solve the random number guessing game in order to receive a flag

### Introduction
To start our process, the team analyzed the function in Ghidra, looking at how it works. They used the function "rand()", located in a C library, where it's job is to generate random number sequences using the current time as the seed. This plays into the time function being used, because it is needed to collect the time elapsed since the EPOCH in order to be used as a seed. It then comes to attention that to be able to get the correct number sequence, we must first get the same seed.

### Program Setup
The team began to curate a Python Program to be able to generate the correct number, while running into certain problems. One of the problems occured due to the fact that the original code was writted in C, and the team was working in Python. To counterract this, the team wrapped a C library thats translates between Python and C calls to be able to borderline use these C calls correctly. The name of the program is "Ctype". 
Using the Ctype library, the python code was curated, using current time as a seed, with pwntools to link with the process. 

The code is below:
`

#!/usr/bin/env python3

#Import the CDLL function from the ctypes library to use C standard library functions
from ctypes import CDLL

#Load the C standard library
libc = CDLL("libc.so.6")

#Get the current time in seconds since the Epoch
k = libc.time(0)  # Retrieve the current time to use as a seed for srand

#Seed the random number generator with the current time
libc.srand(k)  # Seed the random number generator using the current time

#Generate a random number
w = libc.rand()  # Generate a random number using the seeded generator

#Import the process function from the pwntools library
from pwn import *

#Start a new process running the 'time' program
io = process('./time')  # Execute the challenge binary

#Receive output from the 'time' process until the prompt 'Enter your number: ' is received
print(io.recvuntil(b'Enter your number: '))  # Wait for the prompt asking for the number

#Send the generated random number to the 'time' process
io.sendline(b'%d' % w)  # Send the previously generated random number as input

#Receive and print all remaining output from the 'time' process
print(io.recvall())  # Output the response from the challenge process
`

