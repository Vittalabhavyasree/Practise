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
    temp.next=head.next
    printlinkedlist(head)
    #print(getMiddle(head))
    #print(detectloop(head))
    #print(loopfirstnode(head))
    #print(countnodeinloop(head))
    #print(deletemiddle(head))
def printlinkedlist(head):
    temp=head
    while(temp):
        print(temp.val)
        temp=temp.next
def deletedmiddle(self, arr):
    if(head.next==None):
        return None
    slow=head
    fast=head
    prev=None
    while(fast and fast.next):
        prev=slow
        slow=slow=slow.next
        fast=fast.next.next
    prev.next=slow.next
    slow.next=None
    return head
def getMiddle(self,head):
    slow=head
    fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
    return slow.val
def detectloop(self,head):

arr=list(map(int,input().split()))
createlinkedlist(arr)