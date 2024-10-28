class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self):
        current_node = self.head
        result = ''
        while current_node:
            result += str(current_node.data) + ' ---> '
            current_node = current_node.next_node
        return result


first_node = Node("John")
linkedList = LinkedList()
linkedList.insert(first_node)

second_node = Node('Ben')
secondInList = linkedList.insert(second_node)

third_node = Node('Shally')
thirdInList = linkedList.insert(third_node)

print(linkedList)
