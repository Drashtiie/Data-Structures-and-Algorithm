
def preorder(root,ans):
    if root == None:
        return
    ans.append(root.val)
    preorder(root.left, ans)
    preorder(root.right,ans)
    return ans



# inorder

l = []
def inorder(root):
    global l
    if root == None:
        return
    inorder(root.left)
    l.append(root.val)
    inorder(root.right)
    return l



# postorder



def postorder(root,ans):
    if root == None:
        return
    postorder(root.left, ans)
    
    postorder(root.right,ans)
    ans.append(root.val)

    return ans