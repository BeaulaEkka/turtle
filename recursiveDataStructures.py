"""# Recursive Data Structures
26 min

Data structures can also be recursive.

Trees are a recursive data structure because their definition is self-referential. A tree is a data structure which contains a piece of data and references to other trees!

Trees which are referenced by other trees are known as children. Trees which hold references to other trees are known as the parents.

A tree can be both parent and child. We’re going to write a recursive function that builds a special type of tree: a binary search tree.

Binary search trees:

    Reference two children at most per tree node.
    The “left” child of the tree must contain a value lesser than its parent
    The “right” child of the tree must contain a value greater than its parent.

Trees are an abstract data type, meaning we can implement our version in a number of ways as long as we follow the rules above.

For the purposes of this exercise, we’ll use the humble Python dictionary:

bst_tree_node = {"data": 42}
bst_tree_node["left_child"] = {"data": 36}
bst_tree_node["right_child"] = {"data": 73}

bst_tree_node["data"] > bst_tree_node["left_child"]["data"]
# True
bst_tree_node["data"] < bst_tree_node["right_child"]["data"]
# True

We can also assume our function will receive a sorted list of values as input.

This is necessary to construct the
Preview: Docs Loading link description
binary search tree
because we’ll be relying on the ordering of the list input.

Our high-level strategy before moving through the checkpoints.

Base case: The input list is empty

Return "No Child" to represent the lack of node Recursive step: The input list must be divided into two halves
Find the middle
Preview: Docs Loading link description
index
of the list
Store the value located at the middle index
Make a tree node with a "data" key set to the value
Assign tree node’s "left child" to a recursive call using the left half of the list
Assign tree node’s "right child" to a recursive call using the right half of the list
Return the tree node
"""
