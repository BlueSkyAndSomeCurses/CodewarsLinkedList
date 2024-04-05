class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def get_nth(node, index):
    if index < 0:
        raise IndexError("Invalid index value should throw error.")

    if node is None:
        raise IndexError("None linked list should throw error.")

    for i in range(index):
        if node is None:
            raise IndexError("Invalid index value should throw error.")
        node = node.next

    if node is None:
        raise IndexError("Invalid index value should throw error.")
    return node
