#import the deque library
from collections import deque
#create a new empty stack

stack = deque()

# push item into the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# print the stack contents

print(stack)

#pop an item off the stack
print(stack.popleft())

# print the stack after pop call
print(stack)
