class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=Node()


    def length(self):
        CurrentNode=self.head
        total=0
        while CurrentNode.next!=None:
            total+=1
            CurrentNode=CurrentNode.next
        return total

    def display(self):

        elements=[]
        Node = self.head
        while Node:
            elements.append(Node.data)
            Node = Node.next

        print(elements)

    def AppendBeginning(self,newdata):
        newNode =   Node(newdata)
        newNode.next= self.head
        self.head = newNode
    def append(self,data):
        if self.head.data is None:
            self.head.data = data
            self.head.next = None
        else:
            lastNode = self.head
            while lastNode.next is not None:
                lastNode = lastNode.next

            lastNode.next = Node(data=data)

    
    def Insertafteranelement(self,x,data):
        currentNode= self.head

        while currentNode.next is not None:

            if currentNode.data==x:
                break
            else:
                currentNode=currentNode.next
        
        if currentNode is None:
            
            newNode=Node(data)
            currentNode=newNode
        else:

            newNode=Node(data)
            newNode.next=currentNode.next
            currentNode.next=newNode
    def Insertbeforeanelement(self,x,data):
        currentNode= self.head

        while currentNode.next is not None:
            if currentNode.next.data==x:
                break
            else:
                currentNode=currentNode.next
        
        if currentNode is None:
            
            newNode=Node(data)
            currentNode=newNode
        else:

            newNode=Node(data)
            newNode.next=currentNode.next
            currentNode.next=newNode

    def DeleteBeginning(self):
        if self.head is None:
            return
        else:
            self.head=self.head.next

    def DeleteEnd(self):
        if self.head is None:
            return
        currentNode=self.head
        while currentNode.next.next is not None:
            
            currentNode=currentNode.next
        
        currentNode.next=None
    def DeleteItem(self,x):
        if self.head is None:
            return
        currentNode=self.head

        while currentNode.next:

            if currentNode.next.data==x:
                
                currentNode.next=currentNode.next.next
                break
            else:
                currentNode=currentNode.next

my_list=LinkedList()

my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list.display()

my_list.AppendBeginning(4)

my_list.display()
my_list.Insertafteranelement(2,6)
my_list.Insertafteranelement(5,5)
my_list.display()
my_list.Insertbeforeanelement(2,12)
my_list.Insertbeforeanelement(7,13)
my_list.display()
my_list.DeleteItem(12)
my_list.display()
my_list.DeleteItem(13)
my_list.display()
my_list.DeleteBeginning()
my_list.display()
my_list.DeleteEnd()
my_list.display()
my_list.DeleteItem(6)
my_list.display()
my_list.append(10)
my_list.display()
my_list.DeleteItem(10)
my_list.display()


# Time Complexity of Inserting and Deletion at end O(n)
# Time Complexity of Inserting and Deletion at beginning O(1)
# Time Complexity of Inserting and Deletion at any before and after some specific element for optimum time O(n/2)
