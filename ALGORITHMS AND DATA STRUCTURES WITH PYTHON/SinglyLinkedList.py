class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=node()


    def length(self):
        CurrentNode=self.head
        total=0
        while CurrentNode.next!=None:
            total+=1
            CurrentNode=CurrentNode.next
        return total

    def display(self):

        elements=[]
        node = self.head
        while node:
            elements.append(node.data)
            node = node.next

        print(elements)

    def AppendBeginning(self,newdata):
        newnode =   node(newdata)
        newnode.next= self.head
        self.head = newnode
    def append(self,data):
        if self.head.data is None:
            self.head.data = data
            self.head.next = None
        else:
            lastnode = self.head
            while lastnode.next is not None:
                lastnode = lastnode.next

            lastnode.next = node(data=data)

    
    def Insertafteranelement(self,x,data):
        currentnode= self.head

        while currentnode.next is not None:

            if currentnode.data==x:
                break
            else:
                currentnode=currentnode.next
        
        if currentnode is None:
            
            newnode=node(data)
            currentnode=newnode
        else:

            newnode=node(data)
            newnode.next=currentnode.next
            currentnode.next=newnode
    def Insertbeforeanelement(self,x,data):
        currentnode= self.head

        while currentnode.next is not None:
            if currentnode.next.data==x:
                break
            else:
                currentnode=currentnode.next
        
        if currentnode is None:
            
            newnode=node(data)
            currentnode=newnode
        else:

            newnode=node(data)
            newnode.next=currentnode.next
            currentnode.next=newnode

    def DeleteBeginning(self):
        if self.head is None:
            return
        else:
            self.head=self.head.next

    def DeleteEnd(self):
        if self.head is None:
            return
        currentnode=self.head
        while currentnode.next.next is not None:
            
            currentnode=currentnode.next
        
        currentnode.next=None
    def DeleteItem(self,x):
        if self.head is None:
            return
        currentnode=self.head

        while currentnode.next:

            if currentnode.next.data==x:
                
                currentnode.next=currentnode.next.next
                break
            else:
                currentnode=currentnode.next

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
