class Node:
    def __init__ (self,value):  # Constructor for Node creation
        self.value = value
        self.next = None

class LinkedList:
    def __init__ (self): # Constructor for creating linked list with 1st node
        self.head = None
        self.tail = None
        self.length = 0 # Don't forget to give length = 1 when creating node in linkedlist
        
    def __str__ (self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += f"{temp_node.value}"
            if temp_node.next is not None:
                result += "->"
            temp_node = temp_node.next
        return result
    
    def append(self,value): # O(1)
        new_node = Node(value)  # create node
        if self.head is None:    # If the length is already 0 just create new_node 
            self.head =  new_node   # and make head & tail as new_node  
            self.tail = new_node
        else:                   # If it already has elements,
            self.tail.next = new_node   # then make new_node was tail.next
            self.tail = new_node
        self.length += 1        # Increase length
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head   # Making the pointer of the new_node to point towards the self.head (element)
            self.head = new_node    # Now assigning self.head as the new_node
        self.length += 1            # Increasing the length once prepended    
        
    def insert(self,value,index):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
        
new_linked_list = LinkedList()

new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)

print(new_linked_list)

new_linked_list.insert(0,0)

print(new_linked_list)

new_linked_list.insert(25,3)

print(new_linked_list)

new_linked_list.insert(50,6)

print(new_linked_list)

print("This is head: ",new_linked_list.head.value)
print("This is tail: ",new_linked_list.tail.value)