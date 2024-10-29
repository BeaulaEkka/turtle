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
            new_node = self.head
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self):
        current_node = self.head
        all_nodes = []
        while current_node:
            all_nodes.append(str(current_node.data))
            current_node = current_node.next_node
        return "-->".join(all_nodes)


Ll = LinkedList()
Ll.insert_at_head('Robin')
Ll.insert_at_head('Rahul')
Ll.insert_at_head('Rohan')
Ll.insert_at_tail('Mary')
Ll.insert_at_head('Beaula')
print(Ll)
