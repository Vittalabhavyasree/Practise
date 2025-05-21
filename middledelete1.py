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
    return head
