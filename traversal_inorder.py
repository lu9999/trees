from tree_node import Node


class inorder:
    def __init__(self, root):
        self.cache = [root]

    def has_next(self):
        if len(self.cache) > 0:
            return True
        else:
            return False

    def get_next(self):
        output_node = self.cache.pop(0)

        if output_node.right is not None:
            self.cache.insert(0, output_node.right)
        if output_node.left is not None:
            self.cache.insert(0, output_node.left)

        return  output_node

node1 = Node(2)
node2 = Node(3)
node12 = Node(1, node1, node2)

node3 = Node(7)
node03 = Node(9, None, node3)

node_root = Node(6, node12, node03)

x = inorder(node_root)
while x.has_next():
    print x.get_next().value