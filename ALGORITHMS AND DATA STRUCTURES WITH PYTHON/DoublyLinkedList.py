
class Node:
    def __init__(self,data=None):
        self.prev=None
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=Node()

    def display(self):
        elements=[]
        currentnode=self.head
        while currentnode:
            elements.append(currentnode.data)
            currentnode=currentnode.next
        print(elements)
    def AppendBeginning(self,newdata):
        newnode=Node(newdata)
        if self.head.data is None:
            newnode.next=self.head.prev
            self.head=newnode
            return
        else:
            newnode.next=self.head
            self.head=newnode
            
    def AppendEnd(self,newdata):
        newnode=Node(newdata)
        currentnode=self.head
        if self.head.data is None:
            newnode.next=self.head.prev
            self.head=newnode
            return
        else:
            while currentnode.next is not None:
                currentnode=currentnode.next
            newnode.prev=currentnode.next
            currentnode.next=newnode

    def InsertBefore(self,x,newdata):
        newnode=Node(newdata)
        currentnode=self.head
        if self.head.data is None:
            newnode.next=self.head.prev
            self.head=newnode
            return
        else:
            while currentnode.next is not None:
                if currentnode.next.data==x:
                    break
                else:
                    currentnode=currentnode.next
            newnode.next=currentnode.next
            newnode.prev=currentnode
            currentnode.next=newnode
    def InsertAfter(self,x,newdata):
        newnode=Node(newdata)
        currentnode=self.head
        if self.head.data is None:
            newnode.next=self.head.prev
            self.head=newnode
            return
        else:
            while currentnode.next is not None:
                if currentnode.data==x:
                    break
                else:
                    currentnode=currentnode.next
            newnode.next=currentnode.next
            newnode.prev=currentnode
            currentnode.next=newnode
    
MyList=LinkedList()
MyList.display()
MyList.AppendEnd(6)
MyList.display()
MyList.AppendBeginning(1)
MyList.display()
MyList.AppendBeginning(2)
MyList.display()
MyList.AppendBeginning(3)
MyList.display()
MyList.AppendEnd(4)
MyList.display()
MyList.AppendEnd(5)
MyList.display()
MyList.InsertBefore(1,7)
MyList.display()
MyList.InsertBefore(10,8)
MyList.display()
MyList.InsertBefore(10,9)
MyList.display()
MyList.InsertAfter(5,10)
MyList.display()
MyList.InsertAfter(2,11)
MyList.display()
MyList.InsertAfter(15,12)
MyList.display()