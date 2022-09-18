# Queue Implementation with List

from hashlib import new
from math import fabs
from operator import ne


def QueueListImplementation():
    """An empty list was first created at first, than enqueue,dequeue and other operation was made. """
    List=[]
    # Push
    print("At first enqueue some items in list")
    List.append(1)
    List.append(2)
    List.append(3)
    List.append(4)
    print(List)
    # Pop
    print("Now one item will dequeued from list.")
    print(List.pop(0))
    print(List)
    # Top
    print("Right now,the item which is at the top of the queue shown below.")
    print(List[0])
    # Is_empty
    print("Is list is emty was checked as below.")
    print(List.__len__()==0)
    # Length
    print("Lastly length of the list was also shown.")
    print(List.__len__())
# QueueListImplementation()

class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Queue:
    "Queue class implementation with various type of property."
    
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0


    def enqueue(self,newdata):
        newnode=Node(data=newdata)
        if self.head is None:
            self.head = self.tail=newnode
            self.size+=1
        else:
            self.tail.next=newnode
            self.tail=self.tail.next
            self.size+=1

    def display(self):
        elements=[]
        currentnode=self.head
        while currentnode:
            elements.append(currentnode.data)
            currentnode=currentnode.next
        print(elements)    
    def GetSize(self):
        return self.size
    
    def dequeue(self):
        if self.head is None:
            return
        else:
            self.head=self.head.next
            self.size-=1
    def firstelementofqueue(self):
        if self.head is None:
            return None
        else:
            return self.head.data
    def elementendofqueue(self):
        if self.head is None:
            return None
        else:
            return self.tail.data
    def IsEmpty(self):
        return self.size==0
def ClassQueueImplementation():
    ClassQueue=Queue()
    print("Lets enqueue some elements to queue, which is specificly 1,2,3,4,5,6")
    ClassQueue.enqueue(1)
    ClassQueue.enqueue(2)
    ClassQueue.enqueue(3)
    ClassQueue.enqueue(4)
    ClassQueue.enqueue(5)
    ClassQueue.enqueue(6)
    print("The elements of the queue is as follows.")
    ClassQueue.display()
    ClassQueue.dequeue()
    ClassQueue.dequeue()
    print("After dequeuing elements of the queue is as follows.")
    ClassQueue.display()


    print("The size information of the queue is as follows.")
    print(ClassQueue.GetSize())
    print("Element at the beginning of the queue.")
    print(ClassQueue.firstelementofqueue())
    print("Element at the end of the queue.")
    print(ClassQueue.elementendofqueue())
    print("The result of whether the queue is empty or not is as follows.")
    print(ClassQueue.IsEmpty())
# ClassQueueImplementation()

# Time complexity of any case in queue is O(1),except display which is need O(n), however for some worst cases, some problematic situations maybe occur. For this case complexity for enqueue and dequeue will be O(n).

# Also using collections to create Queue

from collections import deque

def CollectionsImplementations():
    newqueue=deque()
    newqueue.append(1)
    newqueue.append(2)
    newqueue.append(3)
    print("The all elements in Queue as shown below.")
    print(newqueue)
    print("Dequeuing an element from Queue.")
    print(newqueue.popleft())
    print("Queue elements after removing one element.")
    print(newqueue)
    print("Get length of queue.")
    print(newqueue.__len__())
# CollectionsImplementations()