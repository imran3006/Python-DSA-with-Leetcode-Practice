"""
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.
  
"""


def finalValueAfterOperation(operations):
    x=0
    for operation in operations:
        if operation == "++x" or operation == "x++":
            x=x+1

        elif operation == "--x" or operation == "x--":
            x=x-1    

    return x

print(finalValueAfterOperation(["--X","X++","X++"]))        

        
