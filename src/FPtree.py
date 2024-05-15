
**src/fp_tree.py**

```python
class Node:
    def __init__(self, item, parent):
        self.item = item
        self.count = 1
        self.parent = parent
        self.children = {}

class FPTree:
    def __init__(self):
        self.root = Node("Null", None)
        self.headers = {}

    def insert_tree(self, items, item_constraints):
        current_node = self.root
        for item in items:
            if item in item_constraints:
                if item in current_node.children:
                    current_node.children[item].count += 1
                else:
                    new_node = Node(item, current_node)
                    current_node.children[item] = new_node
                    if item in self.headers:
                        self.headers[item].append(new_node)
                    else:
                        self.headers[item] = [new_node]
                current_node = current_node.children[item]

# Example usage
if __name__ == "__main__":
    tree = FPTree()
    dataset = [['milk', 'bread', 'butter'], ['bread', 'butter'], ['milk']]
    constraints = {'milk', 'butter'}  # These items must appear in all rules
    for data in dataset:
        tree.insert_tree(data, constraints)
