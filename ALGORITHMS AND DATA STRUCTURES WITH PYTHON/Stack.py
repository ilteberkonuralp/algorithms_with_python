# Stack Implementation with List
def StackListImplementation():
    """An empty list was first created at first, than push,pop and other operation was made. """
    List=[]
    # Push
    print("At first push some items in list")
    List.append(1)
    List.append(2)
    List.append(3)
    List.append(4)
    print(List)
    # Pop
    print("Now one of the item will popped from list.")
    print(List.pop())
    print(List)
    # Top
    print("Right now,the item which is at the top of the stack shown below.")
    print(List[-1])
    # Is_empty
    print("Is list is emty was checked as below.")
    print(List.__len__()==0)
    # Length
    print("Lastly length of the list was also shown.")
    print(List.__len__())
# StackListImplementation()


# Stack Implementation with List
class Empty(Exception):
    pass
class ArrayStack:
    def __init__(self):
        self._data=[]
        self.size=0
    def __len__(self):
        return self._data.__len__()
    def is_empty(self):
        return self.size==0
    def push(self,newitem):
        self._data.append(newitem)
        self.size+=1
    def top(self):
        if self.is_empty():
            raise Empty("Stack has item in it.")
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty("Stack has item in it.")
        self.size -= 1
        return self._data.pop()

    def __repr__(self):
        return [i for i in self._data]
    
    def listsize(self):
        return self.size
def StackArraywithClass():
    Array=ArrayStack()
    Array.push(5)
    Array.push(3)
    Array.push(6)
    Array.push(4)
    print(Array.__repr__())
    Array.pop()
    print(Array.__repr__())
    print(Array.top())
    print(Array.is_empty())
    print(len(Array))

# StackArraywithClass()
# Complexity of Array operation as below
# push o(1), pop o(1), top o(1), is_empty o(1), len o(1). 

def ReversingArray(array):
    a=ArrayStack()
    a_reversed=[]
    for item in array:
        a.push(item)

    while not a.is_empty():
        a_reversed.append(a.pop())
    return a_reversed

try_list=[100,50,25,5,1]
print(ReversingArray(try_list))

