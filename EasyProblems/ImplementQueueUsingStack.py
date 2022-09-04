
# IMPLEMENT QUEUE USING FIFO STRUCTURE --> STACKS!!

class MyQueue:

    #define datastructure which we are going to use
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    #Pushes element x to the back of the queue
    def push(self, x: int) -> None:
         self.in_stack.append(x)
        
    #Removes the element from the front of the queue and returns it.
    def pop(self) -> int:
        self.peek()
        return self.out_stack.pop()
        
    #Returns the element at the front of the queue.
    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]
    
    #Returns true if the queue is empty, false otherwise.
    def empty(self) -> bool:
        return (not self.in_stack) and (not self.out_stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
