class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)


def display(head):
    current = head
    elements = []
    while current:
        elements.append(str(current.val))
        current = current.next
    print(' <--> '.join(elements))


# Insert at the beginning
def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head)
    if head:
        head.prev = new_node
    else:
        tail = new_node  # If the list is empty, the new node is also the tail
    return new_node, tail


# Creating a doubly linked list with one node
head = tail = DoublyNode(1)

# Insert a new node at the beginning
head, tail = insert_at_beginning(head, tail, 3)
head, tail = insert_at_beginning(head, tail, 5)

# Display the list
display(head)
