class NodeList():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(head1, head2):
    dummy = NodeList()
    curr = dummy

    while head1 and head2:
        if head1.val < head2.vale:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next
    
    if head1 or head2:
        curr.next = head1 if head1 else head2

    return dummy.next