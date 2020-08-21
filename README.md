Simple word machine created in python3.
-----------------------------------------------------------------------

A word machine is a system that performs a sequence of simple operations on a stack of integers. initially the stack is empty. The sequence of operations is given as a string. Operations are separated by single spaces.

-----------------------------------------------------------------------
Recognized input:
-----------------------------------------------------------------------
    Integer X:  put a number onto the stack

    POP:        takes number off the top of stack

    DUP:        pops first two numbers off stack, multiplies them pushes result to top of stack
    +:          pops the top most two numbers off stack, adds them, pushes result to the top of the stack
    -:          pops the top most two numbers off stack, subtracts them, pushes result to the top of the stack
All other input is ignored.
The program does not accept numbers greater than 2^20-1
Two integers must be on the stack to execute any math operations
The program outputs the top most number in the stack as the final output.
-----------------------------------------------------------------------
Prerequisites
-----------------------------------------------------------------------
The program can run in any operating system.
To run the program you need the following in your system:

     1. python3 -download from python.org
     2. terminal/cmd/python shell
-----------------------------------------------------------------------
Installing
-----------------------------------------------------------------------
To run the program locally move to the directory containing the program scripts using the cd command
and run the command.

    python3 operations.py  
   or drag the file to the command prompt in windows os

Example inputs:

    13 DUP 4 POP 5 DUP + DUP + -
Expected output:

    10
