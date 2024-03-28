from levelorder import leveloredr
from traversals import inorder, preorder, postorder
from height import height
class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None


root = Node(5)
root.left = Node(6)
root.right = Node(7)
root.left.right = Node(8)
# print(root)
print(leveloredr(root))

print(inorder(root))
print(preorder(root, []))
print(postorder(root, []))
print(height(root))