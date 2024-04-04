class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    # Your code goes here.
    if head is None:
        return Node(data)

    new_node = Node(data)
    new_node.next = head

    return new_node


def build_one_two_three():
    head = Node(3)
    head = push(head, 2)
    return push(head, 1)
