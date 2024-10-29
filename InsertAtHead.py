class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def swap_nodes(self, data1, data2):
        if data1 == data2:
            return

        # Find node1 (data1) and its previous node
        prev_node1 = None
        node1 = self.head
        while node1 and node1.data != data1:
            prev_node1 = node1
            node1 = node1.next_node

        # Find node2 (data2) and its previous node
        prev_node2 = None
        node2 = self.head
        if node2 and node2.data != data2:
            prev_node2 = node2
            node2 = node2.next_node

        # If either node1 or node2 is not found, return
        if not node1 or not node2:
            return

        # If node1 is not head, link previous node1 to node2
        if prev_node1:
            prev_node1.next_node = node2
        else:
            self.head = node2  # If node1 is the head, update the head to node2

        # If node2 is not head, link previous node2 to node1
        if prev_node2:
            prev_node2.next_node = node1
        else:
            self.head = node1  # If node2 is the head, update the head to node1

        # Swap next pointers
        node1.next_node, node2.next_node = node2.next_node, node1.next_node

    def __str__(self):
        current_node = self.head
        all_nodes = []
        while current_node:
            all_nodes.append(str(current_node.data))
            current_node = current_node.next_node
        return "-->".join(all_nodes)


# Example usage
Ll = LinkedList()
Ll.insert_at_head('Robin')
Ll.insert_at_head('Rahul')
Ll.insert_at_head('Rohan')
Ll.insert_at_tail('Mary')
Ll.insert_at_head('Beaula')

print("Before swapping:")
print(Ll)  # Output: Beaula-->Rohan-->Rahul-->Robin-->Mary

# Swap Robin and Rohan
Ll.swap_nodes('Robin', 'Rohan')

print("\nAfter swapping:")
print(Ll)  # Output: Beaula-->Robin-->Rahul-->Rohan-->Mary

#-------------------------------------------------------
print("Before Swapping")
print(Ll)
# Output: Beaula-->Robin-->Rahul-->Rohan-->Mary
# Swap Robin and Rohan
Ll.swap_nodes('Rahul', 'Robin')

print("\nAfter swapping:")
print(Ll) 
# Beaula-->Rahul-->Robin-->Rohan-->Mary
