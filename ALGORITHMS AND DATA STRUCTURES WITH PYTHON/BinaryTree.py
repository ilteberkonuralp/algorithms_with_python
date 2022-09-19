# First Create binary node
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

if __name__=="__main__":
    root=Node(5)

    root.left=Node(3)
    root.right=Node(4)
    root.left.left=Node(2)
    print(root.left.data)
    # Depth First Traversals
    def Inorder():
        pass
    def Preorder():
        pass
    def Postorder():
        pass

