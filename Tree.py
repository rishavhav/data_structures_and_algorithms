class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def contains(self, value):
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def __r_contains(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)



    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        return self.__r_insert(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __r_delete(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left =  self.__r_delete(current_node.left, value)
        if value > current_node.value:
            current_node.right =  self.__r_delete(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.right is None:
                return current_node.left
            elif current_node.left is None:
                return current_node.right
            else:
                min_value = self.min_value(current_node.right)
                current_node.value = min_value
                return self.__r_delete(current_node.right, min_value)
        return current_node


    def r_delete(self, value):
        return self.__r_delete(self.root, value)

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right



my_tree = BinarySearchTree()
print(my_tree.root)

my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)

print('===contains===')
print(my_tree.r_contains(3))

print('===insert===')
my_tree.r_insert(34)
