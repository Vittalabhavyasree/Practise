def levelOrder(root):
    if(root==None):
        return
    q=[root]
    ans=[]
    while(q):
        node=q.pop(0)
        if(node.left!=None):
            q.append(node.left)
        if(node.right!=None):
            q.append(node.right)
        ans.append(node.val)
    return ans
root=list(map(int,input().split(",")))
print(levelOrder(root))