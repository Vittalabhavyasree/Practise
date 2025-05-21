class Node:
    def __init__(self,data):
        self.prev=None
        self.val=data
        self.next=None
def createdoublylist(arr):
    head=None
    for data in arr:
        if(head==None):
            head=Node(data)
            temp=head
        else:
            newNode=Node(data)
            temp.next=newNodes
            newNode.prev=temp
            temp=temp.next
    printdoublylist(head)
def printdoublylist(head):
    temp=head
    while(temp):
        print(temp.val,end=" ")
        temp=temp.next
arr=list(map(int,input().split()))
createdoublylist(arr)
