# babypwn Challenge Documentation

Sure, here's the rewritten version:

## **Create a Directory for Babypwn Files**

   We started by creating a directory for the babypwn files and then moved those files into this directory.

## **Execute the `file` Command**

   We used the `file` command on the files within the directory to get details such as their types and names.

## **Check File Security**

   We verified the security of the files using the `checksec` command to ensure they were secure.

## **Examine Source Code**

   We opened a text editor to view the C file source code. During our examination, we identified potential flaws. For example, there was a character array with a maximum size of 32 bytes, but an input statement allowed for 64 bytes. This discrepancy could lead to a buffer overflow, where a user could input more data than the array can hold.

## **Buffer Overflow**

   A buffer overflow occurs when a program writes more data to a buffer than it can hold, causing the excess data to overflow into adjacent memory locations. This can result in issues such as overwriting the return address of a function, leading to potential security vulnerabilities.

## **Make Exploit Code**
Code used to exploit vulnerabilities in this challenge :
<code>
 
 from pwn import *
 
 #Start the process
 pw = process('babypwn')

 #Attach gdb debugger
 gdb.attach(pw, '''continue''')

 #Interact with the process
 pw.Interactive()

</code>

6. **Access the Babypwn Process with gdb**

   This code allows us to attach to the babypwn process and use the gdb debugger to observe what happens when we input more characters than the array can handle.

7. **Detect Segmentation Fault**

   After inputting more characters than allowed, we detected a segmentation fault, indicating the code tried to execute a program without proper permissions.

8. **Exploit to Capture the Flag**

   The segmentation fault was instrumental in capturing the flag, as we were able to exploit this vulnerability in the challenge.

   **Debugger Output:**

   ```
   Program received signal SIGSEGV, Segmentation fault.
   0x00000000004012c3 in main ()
   ```

$rcx : 0x0

$rdx : 0x0

$rsp : 0x00007fffffffddb8 → 0x0041414141414141 ("AAAAAAA"?)

$rbp : 0x4141414141414141 ("AAAAAAAA"?)

$rsi : 0x00007fffffffd7b0 → ""This is the flag we win"\n"

$rdi : 0x00007fffffffd780 → 0x00007fffffffd7b0 → ""This is the flag we win"\n"

$rip : 0x00000000004012c3 → <main+00aa> ret

$r15 : 0x0

$eflags: [zero carry parity adjust sign trap INTERRUPT direction overflow RESUME virtualx86 identification]

$cs: 0x33 $ss: 0x2b $ds: 0x00 $es: 0x00 $fs: 0x00 $gs: 0x00


