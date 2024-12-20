# Import necessary classes for linked lists and flower definitions
from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

# Define the HashMap class


class HashMap:
    def __init__(self, size):
        self.array_size = size
        # Create an array of LinkedList objects
        self.array = [LinkedList() for _ in range(size)]

    # Hash function to get a numeric code from the key
    def hash(self, key):
        key_bytes = key.encode()
        return sum(key_bytes)

    # Compressor function to ensure hash code is within array bounds
    def compress(self, hash_code):
        return hash_code % self.array_size

    # Assign method to add key-value pairs to the hash map
    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]

        # Check if key already exists in the linked list
        for item in list_at_array:
            if item[0] == key:
                item[1] = value
                return

        # If key is not found, insert the new payload
        list_at_array.insert(payload)

    # Retrieve method to get values by key
    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]

        # Search for the key in the linked list at this index
        for item in list_at_index:
            if item[0] == key:
                return item[1]

        # Return None if key is not found
        return None


# Create a new instance of HashMap with the length of flower_definitions
blossom = HashMap(len(flower_definitions))

# Populate the hash map with flower definitions
for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

# Retrieve a flower's meaning and print it
print(blossom.retrieve('daisy'))
