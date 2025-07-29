class Node:
    def __init__ (self,value):  # Constructor for Node creation
        self.value = value
        self.next = None

class LinkedList:
    def __init__ (self,value): # Constructor for creating linked list with 1st node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 # Don't forget to give length = 1 when creating node in linkedlist
        
    def print_list(self): # O(n)
        temp = self.head    # Let temp be the first element - head
        while temp is not None:
            print(temp.value)   # print its value
            temp = temp.next    # Let the temp iterate till it reaches None for printing the whole linkedlist
    
    def append(self,value): # O(1)
        new_node = Node(value)  # create node
        if self.length == 0:    # If the length is already 0 just create new_node 
            self.head =  new_node   # and make head & tail as new_node  
            self.tail = new_node
        else:                   # If it already has elements,
            self.tail.next = new_node   # then make new_node was tail.next
            self.tail = new_node
            self.length += 1        # Increase length
    
    def pop(self): #O(n)
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre # Take back the tail to pre - previous element to the end
        self.tail.next = None   # Make the tail pointer towards the None. This means freeing the pointer from the old one.
        if self.length == 0:    # Why this? To check if we reduced the linkedlist to 0.
            self.head = None    # If so, we are making the head & tail point towards None
            self.tail = None
        return temp # Returning the popped element
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head   # Making the pointer of the new_node to point towards the self.head (element)
            self.head = new_node    # Now assigning self.head as the new_node
        self.length += 1            # Increasing the length once prepended
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
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self,value,index):
        temp = self.get(index)
        if temp:
            temp.value = value
            return temp
        else:
            return False
        
    def insert(self,value,index):
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        if index < 0 or index > self.length:
            return False
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return temp
    
    def remove(self,index):
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        if index < 0 or index >= self.length:
            return False
        pre = self.get(index-1)
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
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
my_linked_list = LinkedList(1)

print("Initial linked_list: ")
my_linked_list.print_list()
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print("linked_list after append operations: ")
my_linked_list.print_list()

print("linked_list before pop: ")
my_linked_list.print_list()

print("pop element: ")
print(my_linked_list.pop().value)

print("linked_list after pop: ")
my_linked_list.print_list()

print("linked_list before prepend: ")
my_linked_list.print_list()

my_linked_list.prepend(0)

print("linked_list after prepand: ")
my_linked_list.print_list()

print("linked_list before pop_first: ")
my_linked_list.print_list()

print("pop_first_element: ")
print(my_linked_list.pop_first().value)

print("linked_list after pop_first: ")
my_linked_list.print_list()

print("linked_list before get: ")
my_linked_list.print_list()

print("get element: ")
print(my_linked_list.get(2).value)

print("linked_list after get: ")
my_linked_list.print_list()

print("linked_list before set: ")
my_linked_list.print_list()

print("set element: ")
print(my_linked_list.set_value(2,2).value)

print("linked_list after set: ")
my_linked_list.print_list()

print("linked_list before insert: ")
my_linked_list.print_list()

print("insert element: ")
print(my_linked_list.insert(3,3).value)

print("linked_list after insert: ")
my_linked_list.print_list()

print("linked_list before remove: ")
my_linked_list.print_list()

print("remove element: ")
print(my_linked_list.remove(3).value)

print("linked_list after remove: ")
my_linked_list.print_list()

print("linked_list before reverse: ")
my_linked_list.print_list()

my_linked_list.reverse()

print("linked_list after remove: ")
my_linked_list.print_list()