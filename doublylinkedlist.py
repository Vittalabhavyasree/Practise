class Node:
    def __init__(self,data):
        self.prev=None
        self.val=data
        self.next=None
def createDoublylinkedlist(arr):
    head=None
    for data in arr:
        if(head==None):
            head=Node(data)
            temp=head
        else:
            newNode=Node(data)
            temp.next=newNode
            newNode.prev=temp
            temp=temp.next
    temp.next=head.next
    printDoublylinkedlist(head)
def printDoublylinkedlist(head):
    temp=head
    while(temp):
        print(temp.val)
        temp=temp.next
arr=list(map(int,input().split()))
createlinkedlist(arr)