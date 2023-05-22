class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow


my_linked_list = LinkedList(1)
my_linked_list.append(10)
my_linked_list.print_list()
print("length is: " + str(my_linked_list.length))

my_linked_list.pop()
my_linked_list.print_list()
print("length is: " + str(my_linked_list.length))

my_linked_list.pop()
my_linked_list.print_list()
print("length is: " + str(my_linked_list.length))

my_linked_list.prepend(10)
my_linked_list.prepend(20)

my_linked_list.print_list()

print("popped first number: " + str(my_linked_list.pop_first()))
my_linked_list.print_list()

my_linked_list.append(40)
my_linked_list.append(50)

print(my_linked_list.get(2).value)

my_linked_list.set_value(2, 43)
print(my_linked_list.get(2).value)

print("===========LL==============")
my_linked_list.print_list()

print("===========LL==============")
my_linked_list.insert(1, 49)
my_linked_list.print_list()


print("===========LL remove==============")
my_linked_list.remove(2)
my_linked_list.print_list()

print("===========LL==============")
print(my_linked_list.head.value)
print(my_linked_list.tail.value)
print(my_linked_list.length)

print("===========LL reverse==============")
my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.print_list()

print("=============LL middle=================")
print(my_linked_list.find_middle_node().value)
