class TreeNode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
def create_btree(arr,i,n):
    if i>n:
        return None
    root=TreeNode(arr[i-1])
    root_left=create_btree(arr,2*i,n)
    root_right=create_btree(arr,2*i+1,n)
    return root
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
    
    
arr=[3,4,5,6,7,8,9,0]
binarytree=create_btree(arr,1,len(arr))
print("\n  inorder")
inorder(binarytree)
