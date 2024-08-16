# angr crackme Documentation

This document outlines steps to identify and exploit a buffer overflow vulnerability using tools like Ghidra, angr libray, virtual environment, and Python.
## Utilizing Ghidra

Ghidra is an open-source tool utilized for reverse engineering, which allows you to decompile and analyze binary files

1. We created a new project in Ghidra
2. The binary wa imported into the project, setting it up to be analyzed
3. We looked into the functions, searching for clues, details, and possible problems that could consist of the code
4. We fished out a specific function inside the source code

## Code and File

Our goal im Ghidra is to identify vulnerabilities that could be present in the code, where we were able to note different function calls that were used

- There was a function call to puts that prints out the string that shows that the user guess the correct password. There was also another puts call to print when the user guess the password incorrectly. You see for this challenge we are prompeted to entered the corrcect password in order to win. So by knowing where we need to go in memory it will allow us to directly access the win conditon.

- This is when we file the crackme file: crackme: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=a4e83e232e5b2c227eedee6f1c600956577a5cc9, for GNU/Linux 3.2.0, not stripped

i This is when we checksec the crackme file: RELRO STACK CANARY NX PIE RPATH RUNPATH Symbols FORTIFY Fortified Fortifiable FILE Partial RELRO No canary found NX enabled PIE enabled No RPATH No RUNPATH 71 Symbols No 0 1 crackme


## Target Memory Address

After the exploitation of the buffer overflow, having the memory address to return to is an important step to take.

- Use Ghidra to identify the memory address to redirect to
- Record the address to be used in payload to overwrite return address
- The **desired address** is the address in memory to be returned to
- The **wrong address** is the address to avoid.

## Python Program
<code>  
 import angr
 import claripy
 #import code

 #Establish the Angr Project
 target = angr.Project('crackme', main_opts = {'base_addr': 0x0})

 #Specify the desired address which means we have the correct input
 desired_adr = 0x1220


 #Specify the address which if it executes means we don't have the correct input
 wrong_adr = 0x122e

 #Flag is 10 characters
 flag = claripy.BVS("flag", 8 * 10)

 #Establish the entry state
 entry_state = target.factory.entry_state(stdin = flag)

 #Silence the warnings
 entry_state.options.add(angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY)

 #Flags consists only on numbers ('0' -> '9')
 for i in range(10):
     entry_state.solver.add(flag.get_byte(i) >= 48)
     entry_state.solver.add(flag.get_byte(i) <= 57)

 #Establish the simulation
 simulation = target.factory.simulation_manager(entry_state)

 #Start the simulation
 simulation.explore(find = desired_adr, avoid = wrong_adr)

 #code.interact(local=locals())

 solution = simulation.found[0].posix.dumps(0)

 print(solution)

</code>
## Conclusion
When running our Python program, we encountered errors due to the way Python was configured on our system, leading to compatibility issues with some commands and functions in the angr library. To resolve this, we created a virtual environment that allowed us to fully utilize the angr library and successfully obtain the password we needed. Additionally, we leveraged the claripy library, specifically using the `claripy.BVS()` function to create a bitvector representing a symbolic variable for the flag. This proved to be a valuable tool for symbolic execution engines like angr. This documentation outlines the steps taken and our thought process in exploiting the program to achieve the desired results.
