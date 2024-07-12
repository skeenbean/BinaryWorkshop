### babypwn Challenge Solution

# Intro
The team started up by creating a directory for the babypwn and babypwn.c files to be stored. Then, from using the link, the files were downloaded and redirected into the directory

The team then utilized the file command on the babypwn files in order to gather more information on them

A new command called checksec was used to verify the security of the commands


# Source Code Review
Using Text editors, the source code was viewed and examined. There were evident flaws that consisted in the code. In the code, an array was listed with the max size of 32 bytes, even though the input allowed for 64 bytes. This entertains the possibility of a user inputing more than needed, which in turn can cause a buffer overflow. A buffer overflow happens when softwares write too muh data into a bufer, which causes excess data to overflow into different memory locations.


# Code Formulation
The team formulated a program to exploit the problems found in the code. 
The code is listed below

from pwn import *

#Start process
pw = process('babypwn')

#Attach gdb debugger
gdb.attach(pw, '''continue''')

#Interact with the process
pw.Interactive()

# Code Review Continued
When emulating a user inputting an exceeded amount of characters, a segmentation fault occured, meaning the program attempted to execute the program on its own.
The segmentation fault in turn led us to capturing the flag, exploiting the vulnerability

# Conclusion
After reviewing the code, utilizing certain commands, and seeking out vulnerabilities, the team used the buffer overflow in order to collect the flag, and complete the challenge. 
