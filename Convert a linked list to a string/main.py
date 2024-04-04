class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    if node is None:
        return "None"

    outp = str(node.data)

    node = node.next

    while node != None:
        outp += f" -> {node.data}"
        node = node.next

    return outp + " -> None"

