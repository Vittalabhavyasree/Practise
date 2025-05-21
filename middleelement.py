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
    print(getmiddle(head))
def getmiddle(head):
    slow=head
    fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
    return slow.val
def printlinkedlist(head):
    temp=head
    while(temp):
        print(temp.val,end=" ")
        temp=temp.next
arr=list(map(int,input().split()))
createlinkedlist(arr)
