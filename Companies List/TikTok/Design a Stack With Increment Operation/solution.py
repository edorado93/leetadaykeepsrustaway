class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.inc = [0 for _ in range(maxSize + 1)]
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        
        # Don't push beyond capacity
        if len(self.stack) == self.maxSize:
            return
        
        # Push an element at the top
        self.stack.append(x)

    def pop(self) -> int:
        
        if not self.stack:
            return -1
        
        sz = len(self.stack)
        
        # Since we have incorporated the inc[sz] information
        # while popping, we "pass along" the information for the
        # previous elements.
        ret_val = self.stack.pop() + self.inc[sz]
        
        # Pass along the information for the previous information
        self.inc[sz - 1] += self.inc[sz]
        
        # Reset this position as this information has been used
        self.inc[sz] = 0
        return ret_val

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.stack))
        self.inc[k] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
