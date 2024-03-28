def height(node):
    if node == None:
                return 0
           
    return max(height(node.left),height(node.right))+1