# LIFO
class Stack:
    def __init__(self):
        self.elems = []
        # remove last element 
    def pop(self):
        if len(self.elem)==0:
            return "Stack is empty !"
        return self.elems.pop()
    # add a new to top
    def push(self , val):
        self.elems.append(val)
        
    def peek(self):
        if len(self.elem) == 0:
            return "Stack is empty !"
        return self.elems[-1]
    
    def size(self):
        return len(self.elems)
    
    
    def reverse_string(string):
        stack = Stack()
        result =""
         # push all characters
        for char in string:
            stack.push(char)
        
        # pop all characters
        while not stack.is_empty():
            result += stack.pop()
    
        return  result 
        
my_stack= Stack()
my_stack.push(
    1)  
my_stack.push(2)  
my_stack.push(3)  
            
print(my_stack.size())           