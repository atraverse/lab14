from btnode import Node

class Tree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value<cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value>cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print('Value already in tree!')

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None: return cur_height
        left_height = self._height(cur_node.left_child, cur_height+1)
        right_height = self._height(cur_node.right_child, cur_height+1)
        if left_height > right_height:
            return True
        else:
            return False


