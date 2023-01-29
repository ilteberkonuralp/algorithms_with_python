# First Create binary node
class Node:
    def __init__(self, value:int):
        
        self.left = None
        self.right = None
        self.data = value

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
# print(root.left.data)
# Depth First Traversals
def InorderTraversal(root: Node) -> None:
    if root is None:
        return
    InorderTraversal(root.left)
    print(root.data,end=" ")
    
    InorderTraversal(root.right)
    return
# print("Inorder Traversal result:")
# InorderTraversal(root)

def PreorderTraversal(root):
    if root is None:
        return
    print(root.data,end=" ")
    PreorderTraversal(root.left)
    PreorderTraversal(root.right)
# print("\nPreorder Traversal result:")
# PreorderTraversal(root)
def PostorderTraversal(root):
    if root is None:
        return
    
    PreorderTraversal(root.left)
    PreorderTraversal(root.right)
    print(root.data,end=" ")
# print("\nPost order Traversal result:")
# PostorderTraversal(root)
