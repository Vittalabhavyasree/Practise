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
    print(reverse(head))
def reverse(head):
    prev=None
    temp=head
    while(temp):
        front=temp.next
        temp.next=prev
        prev=temp
        temp=front
    return prev.val
def printlinkedlist(head):
    temp=head
    while(temp):
        print(temp.val, end=" ")
        temp=temp.next
arr=list(map(int,input().split()))
createlinkedlist(arr)