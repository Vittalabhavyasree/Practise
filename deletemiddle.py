class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
def createlinkedlist(arr):
    head=None
    for data in arr:
        if(head==None):
            head=Node(data)
            temp=head
        else:
            temp.next=Node(data)
            temp=temp.next
    printlinkedlist(head)
    print(deletemiddle(head))
def deletemiddle(head):
    if (head.next==None):
        return None
    slow=head
    fast=head
    prev=None
    while(fast and fast.next):
        prev=slow
        slow=slow.next
        fast=fast.next
    prev.next=slow.next
    slow.next=None
    return head.data
def printlinkedlist(head):
    temp=head
    while(temp):
        print(temp.val,end=" ")
        temp=temp.next
arr=list(map(int,input().split()))
createlinkedlist(arr)
