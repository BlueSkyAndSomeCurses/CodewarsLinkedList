class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def loop_size(node):
    slow = node
    fast = node.next

    while slow is not fast:
        slow = slow.next
        fast = fast.next.next

    len_ = 1
    slow = slow.next

    while slow is not fast:
        len_ += 1
        slow = slow.next

    return len_


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head.next

print(loop_size(head))
