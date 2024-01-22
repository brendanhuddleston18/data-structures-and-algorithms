from data_structures.stack import Stack


class PseudoQueue:
# Kyle helped me figure this out
    def __init__(self): 
        self.stack_one = Stack()
        self.stack_two = Stack()

    # This pushes the initial value into the first stack
    def enqueue(self, value):
        self.stack_one.push(value)

    # This moves each value from stack one into stack two, then pops the the top value and returns it.  
    def dequeue(self):

        popped_value = None
        
        while self.stack_one.top:
            
            dq_value = self.stack_one.pop()

            self.stack_two.push(dq_value)
        
        if self.stack_two.top:
            popped_value = self.stack_two.pop()
        
        while self.stack_two.top:

            dq_value = self.stack_two.pop()

            self.stack_one.push(dq_value)
        
        return popped_value

