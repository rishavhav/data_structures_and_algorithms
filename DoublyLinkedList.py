class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def pop_first(self):
        if self.length == 0 or self.length == 1:
            return self.pop()
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        if self.length == 0:
            self.append(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    def print_dll(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False



my_doubly_ll = DoublyLinkedList(7)
my_doubly_ll.append(20)
my_doubly_ll.append(34)

my_doubly_ll.print_dll()

print('===pop===')
print(my_doubly_ll.pop().value)
print('length: ' + str(my_doubly_ll.length))
print('===after pop===')
my_doubly_ll.print_dll()
print('length: ' + str(my_doubly_ll.length))
print('===prepend===')
my_doubly_ll.prepend(403)
my_doubly_ll.prepend(65)
my_doubly_ll.prepend(90)
my_doubly_ll.print_dll()

print('===get===')
print(my_doubly_ll.get(3).value)

print('===set===')
print(my_doubly_ll.set(3, 108))
print('===after set===')
my_doubly_ll.print_dll()


