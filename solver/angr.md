# angr Challenge Documentation

 This document details the steps taken to identify and exploit a buffer overflow vulnerability using tools such as Ghidra, the angr library, a virtual environment/ , and Python.
 
## Utilizing Ghidra

Ghidra is an open-source tool utilized for reverse engineering, which allows you to decompile and analyze binary files

1. We created a new project in Ghidra
2. The binary wa imported into the project, setting it up to be analyzed
3. We looked into the functions, searching for clues, details, and possible problems that could consist of the code
4. We fished out a specific function inside the source code

## Code and File

Our goal im Ghidra is to identify vulnerabilities that could be present in the code, where we were able to note different function calls that were used

- We fished out a function call to **puts**. This function prints out string that shows a case where the user guesses the password correctly. Alongside this case, there was another case in the event that a user input the incorrect password. This showed us specifically where we need to go in memory, allowing us to access the win condition.
- We then used the command **file** on the r100 file: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=0f464824cc8ee321ef9a80a799c70b1b6aec8168, stripped
- We then utilized the **checksec** command on the r100 file: RELRO STACK CANARY NX PIE RPATH RUNPATH SymbolsFORTIFY Fortified Fortifiable FILE Partial RELRO Canary found NX enabled No PIE No RPATH No RUNPATH No Symbols No 0 2 r100

## Target Memory Address

After the exploitation of the buffer overflow, having the memory address to return to is an important step to take.

- Use Ghidra to identify the memory address to redirect to
- Record the address to be used in payload to overwrite return address
- The **desired address** is the address in memory to be returned to
- The **wrong address** is the address to avoid.

## Python Program
` # Import Angr
import angr

# Establish the Angr Project
target = angr.Project('r100')

# Specify the desired address which means we have the correct input
desired_adr = 0x00400849 

# Specify the address which if it executes means we don't have the correct input
wrong_adr = 0x0040085a

# Establish the entry state
entry_state = target.factory.entry_state(args=["./fairlight"])

# Establish the simulation
simulation = target.factory.simulation_manager(entry_state)

# Start the simulation
simulation.explore(find = desired_adr, avoid = wrong_adr)

solution = simulation.found[0].posix.dumps(0)
print(solution)
`
## Conclusion
While running through this challenge, we did run into certain errors due to how python was set up on our VM. Certain functions in the angr library were not able to run. To solve this, we created a virtual environment that let us use the angr library in all of its contents, in order to get the correct password. 
