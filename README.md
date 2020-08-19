Simple stack machine created in python3. Input is separated by whitespaces
-----------------------------------------------------------------------
Recognized input:

  [number]      (put a number onto the stack)
  pop           (takes number off the top of stack)

  dup           (pops first two numbers off stack, multiplies them pushes result to top of stack)
  '+'           (pops the top most two numbers off stack, adds them, pushes result to the top of the stack)
  '-'           (pops the top most two numbers off stack, subtracts them, pushes result to the top of the stack)

All other input is ignored.
The program does not accept numbers greater than 2^20-1
Two integers must be on the stack to execute any math operations
-----------------------------------------------------------------------

Example inputs:

    13 DUP 4 POP 5 DUP + DUP + -

Example output:
    7
