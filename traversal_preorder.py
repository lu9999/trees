from tree_node import Node

class preorder:

    def __init__(self, root):
        self.cache = [root]
        current_node = root
        while current_node.left is not None:
            self.cache.append(current_node.left)
            current_node = current_node.left

    def has_next(self):
        if len(self.cache) > 0:
            return True
        else:
            return False

    def get_next(self):
        if len(self.cache) <= 0:
            return -1

        output_node = self.cache.pop()

        if output_node.right is not None:
            self.cache.append(output_node.right)
            current_node = output_node.right
            while current_node.left is not None:
                self.cache.append(current_node)
                current_node = current_node.left
        return output_node


node1 = Node(2)
node2 = Node(3)
node12 = Node(1, node1, node2)

node3 = Node(7)
node03 = Node(9, None, node3)

node_root = Node(6, node12, node03)

x = preorder(node_root)
while x.has_next():
    print x.get_next().value


