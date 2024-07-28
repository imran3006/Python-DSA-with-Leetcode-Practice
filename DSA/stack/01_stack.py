"""
real life exmple of stack is undo/redo of any program
1. list/Array
2. Function
"""

def push(stack,item):
     stack.append(item)
def pop(stack):
     if isEmpty(stack):
          return "stack is empty"
     else:
          return stack.pop()
     
def peek(stack):
     if isEmpty(stack):
          return "stack is empty"
     else:
          return stack[-1]
          

def isEmpty(stack):
     return len(stack) == 0
     

stack = []
push(stack, "ab")
push(stack, "bc")
push(stack, "cd")
push(stack, "da")

print(stack)

print("top element: ", peek(stack))
pop(stack)
print(stack)



