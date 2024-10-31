class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def get_prev_node(self):
        return self.prev_node

    def set_next_node(self, node):
        self.next_node = node

    def set_prev_node(self, node):
        self.prev_node = node


def display(head):
    current_node = head
    elements = []
    while current_node:
        # Use `value` instead of `val`
        elements.append(str(current_node.value))
        current_node = current_node.next_node
    print(' <--> '.join(elements))


class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    # def add_to_head(self, new_value):
    #     new_head = Node(new_value)
    #     current_head = self.head_node

    #     if current_head is not None:
    #         current_head.set_prev_node(new_head)
    #         new_head.set_next_node(current_head)

    #     self.head_node = new_head

    #     if self.tail_node is None:
    #         self.tail_node = new_head

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head:
            current_head.set_prev_node(new_head)

    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node

        if current_tail is not None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail_node = new_tail

        if self.head_node is None:
            self.head_node = new_tail

    def remove_head(self):
        removed_head = self.head_node

        if removed_head is None:
            return None

        self.head_node = removed_head.get_next_node()

        if self.head_node is not None:
            self.head_node.set_prev_node(None)
        else:
            self.tail_node = None  # List is empty

        return removed_head.get_value()

    def remove_tail(self):
        removed_tail = self.tail_node

        if removed_tail is None:
            return None

        self.tail_node = removed_tail.get_prev_node()

        if self.tail_node is not None:
            self.tail_node.set_next_node(None)
        else:
            self.head_node = None  # List is empty

        return removed_tail.get_value()

    def remove_by_value(self, value_to_remove):
        current_node = self.head_node

        while current_node is not None:
            if current_node.get_value() == value_to_remove:
                if current_node == self.head_node:
                    return self.remove_head()
                elif current_node == self.tail_node:
                    return self.remove_tail()
                else:
                    next_node = current_node.get_next_node()
                    prev_node = current_node.get_prev_node()
                    next_node.set_prev_node(prev_node)
                    prev_node.set_next_node(next_node)
                    return current_node.get_value()
            current_node = current_node.get_next_node()

        return None


# Initialize the linked list
doubly_linked_list = DoublyLinkedList()

# Add nodes to the head
doubly_linked_list.add_to_head(5)
doubly_linked_list.add_to_head(10)

# Print the value of the head node
print(doubly_linked_list.head_node.get_value())  # This should output 10

# Display the list
display(doubly_linked_list.head_node)
