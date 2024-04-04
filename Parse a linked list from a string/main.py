class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def linked_list_from_string(s):
    if s == "None":
        return None

    s = s.split(" -> ")

    head = Node(int(s[0]))
    curr = head

    for _, val in enumerate(s[1:]):
        if val != "None":
            curr.next = Node(int(val))
        curr = curr.next

    return head
