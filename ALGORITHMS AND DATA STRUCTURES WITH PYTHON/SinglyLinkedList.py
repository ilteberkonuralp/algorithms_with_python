class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self,head=None):
        self.head=node()

    def append(self,data):
        Newnode=node(data)
        CurrentNode=self.head
        while CurrentNode.next!=None:
            CurrentNode=CurrentNode.next
        CurrentNode.next=Newnode

    def length(self):
        CurrentNode=self.head
        total=0
        while CurrentNode.next!=None:
            total+=1
            CurrentNode=CurrentNode.next
        return total

    def display(self):
        elements=[]
        CurrentNode=self.head
        while CurrentNode.next!=None:
            CurrentNode=CurrentNode.next
            elements.append(CurrentNode.data)
        print(elements)

my_list=LinkedList()

my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()