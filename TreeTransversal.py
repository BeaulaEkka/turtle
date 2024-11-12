# Tree Transversal-O(n)
# IN order
# post order
#
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self, level=0):
        # helper to print tree
        ret = "--->" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

    def add_child(self,child_node):
        self.children.append(child_node)

company=[
    "Monkey business CEO",
    "VP of Bananas",
    "VP of Lazing around",
    "Associate Chimp"
]
root=TreeNode(company.pop(0))


for count in range(2):
    child=TreeNode(company.pop(0))
    root.add_child(child)

root.children[0].add_child(TreeNode(company.pop(0)))
print(root)
