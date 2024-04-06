class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if head is None or head.next is None:
        raise Exception("")

    first = head
    second = head.next
    saved_second = head.next

    ident = True
    curr = head.next.next

    while curr is not None:
        if ident:
            first.next = curr
            first = first.next
        else:
            second.next = curr
            second = second.next

        curr = curr.next
        ident = not ident

    first.next = None
    second.next = None

    return Context(head, saved_second)


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

alternating_split(head)
