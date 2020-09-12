Simple word machine created in python3.
-----------------------------------------------------------------------
A word machine is a system that performs a sequence of simple operations on a stack of integers. Initially the stack is empty.
The sequence of operations is given as a string. Operations are separated by single spaces. The following operations may be specified.

    an integerX(from 0 to 20^20-1): The machine pushes X ionto the machine.
    'POP': the machine removes the topmost number from the stack.
    'DUP': the machine pushes the duplicate of the topmost number in the stack.
    '+': the machine pops the two top most numbers from the stack, adds them together and pushes the sum into the stack.
    '-': the machine pops the two topmost numbers from the stack, subtracts the second one from the first(topmost) and pushes the difference into the stack.
-----------------------------------------------------------------------
   1.After processing of all the operations, the machine returns the topmost number from the stack.
   
   2.The machine processes 20-bit unsigned integers(numbers from 0-2^20-1). An overflow in addition or an underflow in subtraction causes an error.
   
   3.The machine also reports an error when it tries to perform an operation that requires more numbers on the stack than the stack actually contains.
   
   4.Also if after performing the operation the stack is empty, the machine reports an error.
   
-----------------------------------------------------------------------
Recognized input:
-----------------------------------------------------------------------
    Integer X:  put a number onto the stack
    POP:        takes number off the top of stack
    DUP:        pops first two numbers off stack, multiplies them pushes result to top of stack
    +:          pops the top most two numbers off stack, adds them, pushes result to the top of the stack
    -:          pops the top most two numbers off stack, subtracts them, pushes result to the top of the stack
For example, given a string "13 DUP 4 POP 5 DUP + DUP + -", the machine performs the following operations:

    Operation   |  Comment             | stack
    -----------------------------------------------------
    "13"        | push 13              | 13
    "DUP"       | duplicate 13         | 13, 13
    "4"         | push 4               | 13, 13, 4
    "POP"       | pop 4                | 13, 13
    "5"         | push 5               | 13, 13, 5
    "DUP"       | duplicate 5          | 13, 13, 5, 5
    "+"         | add 5 and 5          | 13, 13 10
    "DUP"       | duplicate 10         | 13, 13, 10, 10
     "+"        | add 10 and 10        | 13, 13, 20
     "-"        | subtract 13 from 20  | 13,7
-----------------------------------------------------------------------
Finally, the machine wil return 7.

All other input is ignored.
The program does not accept numbers greater than 2^20-1
Two integers must be on the stack to execute any math operations
The program outputs the top most number in the stack as the final output.

Given a string "5 6 + -", the machine reports an error,since, after the addition,there is only one number on the stack, but subtraction expects two.

Given a string "3 DUP 5 - -", the machine reports an error, since the second subtraction yields a negative result 

-----------------------------------------------------------------------
Prerequisites
-----------------------------------------------------------------------
The program can run in any operating system.
To run the program you need the following in your system:

     1. python3 -download from python.org/pip install python3
     2. terminal/cmd/python shell
-----------------------------------------------------------------------
Installing
-----------------------------------------------------------------------
First you'll need to clone the git hub repository containing the program code locally into your machine.
You can clone using the following commands:

    1. make a new directory/folder where files will be stored:
            eg. mkdir stackMachine
    2. go to the new directory:
            cd stackMachine
    3. then initiate an empty git repository:
            git init
    4. clone the git repositpory containing the program files i.e:
            git clone https://github.com/ellyjohnmwangi/stackmachine.git
    The program files will be copied locally in your computer.
-----------------------------------------------------------------------
Running the tests
-----------------------------------------------------------------------
To run the automated tests, using the terminal or cmd ;
    
    1. change directory to the directorate containing the tests.py file.
    2. run the script using 
        python3 tests.py
-----------------------------------------------------------------------
Deployment
-----------------------------------------------------------------------
Stack machine can be used in real life applications in systems such as:
______________________________________________________________________
   1. Computer algorithms for
        (a). remembering partially completed tasks
        (b). undoing(backtracking from an action)
   2. when a company wants to reduce its work force it can use stack operations to utilize the slogan "last hired, first hired".
   3. used to remember racks that one follows when searching through a graph, network or tree.
   4. back/forward stacks on browsers
   5. reversing strings.
----------------------------------------------------------------------
Built With
----------------------------------------------------------------------
This program is built using:
______________________________________________________________________
   1. python 3.6
----------------------------------------------------------------------
Contributing
----------------------------------------------------------------------
When contributing to this repository, please first discuss the change you want to make via email 
or any other method witg]h the owner of this repository before making any changes.
----------------------------------------------------------------------
Pull Request Process
----------------------------------------------------------------------
  1. Ensure any install or build dependencies are removed at the end of the layerwhen doing 
  a build.
  2. Update the README.md with the details of the changes to the interface, this includes new environment 
  variables,useful file locations and parameters
  3. Increase the version number in any examples file and the README,md to the new version 
  that this pull request would represent.
  4. You may merger the Pull Request in once you have the sign off of the developer, or ifyou do not have 
  the permission to do that you may ask the developer to do it for you.
  