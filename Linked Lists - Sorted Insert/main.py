class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    new_head = Node(data)

    if head is None:
        return new_head

    if head.data > data:
        new_head.next = head
        return new_head

    curr = head

    while curr.next is not None:
        if curr.next.data > data:
            new_head.next = curr.next
            curr.next = new_head
            return head
        curr = curr.next

    curr.next = new_head
    return head
