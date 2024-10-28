class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


# Creating the nodes
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

# Linking the nodes
Head.next = A
A.next = B
B.next = C

# Traverse the list O(n)
curr = Head
while curr:
    print(curr)
    curr = curr.next


# Function to display linked list
def display(head):
    curr = head
    elements = []  # Initialize the list inside the function
    while curr:
        elements.append(str(curr.val))  # Append the value of each node
        curr = curr.next
    print(' -> '.join(elements))  # Print the elements joined by '->'


# Calling the display function
display(Head)

#sear
