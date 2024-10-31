class DoublyNode:
    def __init__(self, val, next_node=None, prev_node=None):
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return str(self.val)


def display(head):
    current_node = head
    elements = []
    while current_node:
        elements.append(str(current_node.val))
        current_node = current_node.next_node
    print(' <--> '.join(elements))


# Insert at the beginning
def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next_node=head)
    if head:
        head.prev_node = new_node
    else:
        tail = new_node  # If the list is empty, the new node is also the tail
    return new_node, tail


# Insert at the tail
def insert_at_tail(head, tail, val):
    new_node = DoublyNode(val, prev_node=tail)
    if tail:
        tail.next_node = new_node
    else:
        head = new_node  # If the list is empty, the new node is also the head
    return head, new_node  # Always return the head and new tail


def remove_head(head, tail):

    if head is None:
        return None, None
    else:
        new_head = head.next_node
        if new_head:
            new_head.prev_node = None
        else:
            tail = None
        return new_head, tail


def remove_tail(head, tail):
    if tail is None:
        return None, None
    else:
        new_tail = tail.prev_node
        if new_tail:
            new_tail.next_node = None
        else:
            head = None  # If the list becomes empty, set head to None as well
        return head, new_tail


def remove_by_value(head, tail, value_to_remove):
    current_node = head

    # transverse to the list to find the value.
    while current_node:
        if current_node.val == value_to_remove:
            # if node is the head
            if current_node == head:
                head, _ = remove_head(head, tail)
                if head is None:
                    tail = None
                return head, tail

            # Node is the tail
            elif current_node == tail:
                tail, _ = remove_tail(head, tail)
                if tail == None:
                    head = None
                    return head, tail

            # Node in the middle
            else:
                prev_node = current_node.prev_node
                next_node = current_node.next_node
                prev_node.next_node = next_node
                next_node.prev_node = prev_node
                return head, tail
        current_node = current_node.next_node

    print("value not found in the list")
    return head, tail

        # Creating a doubly linked list with one node
head = tail = DoublyNode(1)

# Insert new nodes at the beginning
head, tail = insert_at_beginning(head, tail, 3)
head, tail = insert_at_beginning(head, tail, 5)
head, tail = insert_at_beginning(head, tail, 10)
head, tail = insert_at_beginning(head, tail, 7)

# Insert a node at the tail
head, tail = insert_at_tail(head, tail, 40)
head, tail = remove_head(head, tail)
head, tail = remove_tail(head, tail)
head, tail = remove_tail(head, tail)
head,tail =remove_by_value(head,tail,5)
# Display the list
display(head)
