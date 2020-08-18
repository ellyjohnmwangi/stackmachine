Simple stack machine created in python3. Input is separated by whitespaces
-----------------------------------------------------------------------
Recognized input:

  [number]      (put a number onto the stack)
  pop           (takes number off the top of stack)

  dup           (pops first two numbers off stack, multiplies them pushes result to top of stack)
  '+'           (pops the top most two numbers off stack, adds them, pushes result to the top of the stack)
  '-'           (pops the top most two numbers off stack, subtracts them, pushes result to the top of the stack)

All other input is ignored.
Two integers must be on the stack to execute any math operations
-----------------------------------------------------------------------

Example inputs:

    12 DUP 21 9 POP 32 + 12 DUP 5 17 7 -
