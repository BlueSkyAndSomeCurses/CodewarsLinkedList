class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def reverse(head, prev=None):
    if head is None:
        return None

    tail = reverse(head.next, head)
    head.next = prev

    if tail is None:
        return head

    return tail
