from collections import deque

def levelorder(root):
    fifo = deque([root])
    
    while fifo:
        size = len(fifo)
        for _ in range(size):
            node = fifo.popleft()

            if node.left: 
                fifo.append(node.left)
            if node.right: 
                fifo.append(node.right)
