class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def swap_pairs(head):

    if head is None:
        return None

    if head.next is None:
        return head

    second = head.next

    head.next = second.next
    second.next = head

    head = second

    prev = head.next
    curr = head.next.next

    while curr is not None and curr.next is not None:
        prev.next = curr.next
        curr.next = curr.next.next
        prev.next.next = curr

        prev = curr
        curr = prev.next

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print(swap_pairs(head))
