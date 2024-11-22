from collections import deque

arr, stack = [], deque()

for idx, current in enumerate(arr):
    while stack and arr[stack[-1]] < current: # Check `OPERATOR`
        stack_top = stack.pop()

        # do something with stack_top here e.g.
        # next_greater[stack_top] = idx

    if stack:
        pass
        # if stack has some elements left
        # do something with stack top here e.g.
        # previous_greater[idx] = stack[-1]

    # at the end, we push the current index into the stack
    stack.append(idx)
"""
| Problem          | Stack Type            |      `OPERATOR`     | Assignment Position  |
|------------------|-----------------------|---------------------|----------------------|
| next greater     | decreasing (equal ok) | stackTop < current  | inside while loop    |
| previous greater | decreasing (strict)   | stackTop <= current | outside while loop   |
| next smaller     | increasing (equal ok) | stackTop > current  | inside while loop    |
| previous smaller | increasing (strict)   | stackTop >= current | outside while loop   |
"""