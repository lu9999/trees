from tree_node import Node


class postorder:
    def __init__(self, root):
        self.cache = [root]
        while root.right is not None:
            self.cache.append(root.right)
            root = root.right

    def has_next(self):
        if len(self.cache) > 0:
            return True
        else:
            return False

    def get_next(self):
        output_node = self.cache.pop()

        if output_node.left is not None:
            current_node = output_node.left
            self.cache.append(current_node)
            while current_node.right is not None:
                self.cache.append(current_node.right)
                current_node = current_node.right

        return output_node

node1 = Node(2)
node2 = Node(3)
node12 = Node(1, node1, node2)

node3 = Node(7)
node03 = Node(9, None, node3)

node_root = Node(6, node12, node03)

x = postorder(node_root)
while x.has_next():
    print x.get_next().value