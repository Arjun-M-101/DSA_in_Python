class Node:
    def __init__ (self,value): 
        self.value = value
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__ (self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += f"{temp_node.value}"
            if temp_node.next is not None:
                result += "->"
            temp_node = temp_node.next
        return result
    
    def append(self,value): 
        new_node = Node(value)
        if self.head is None: 
            self.head =  new_node  
            self.tail = new_node
        else:                  
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1  
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  
            self.head = new_node 
        self.length += 1           
        
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
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            
    def search(self,target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False
    
    def search_index(self,target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1
    
    def get (self,index):
        if index < -1 or index >= self.length:
            return None
        if index == -1:
            return self.tail
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
new_linked_list = LinkedList()

print("Inital linked_list: ",new_linked_list.head)

new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
print("Appending items, 10, 20, 30, 40: ")
print(new_linked_list)

print("Inserting item 0 at index 0: ")
new_linked_list.insert(0,0)
print(new_linked_list)

print("Inserting item 50 at index 5: ")
new_linked_list.insert(50,5)
print(new_linked_list)

print("Traversing inside the linked-list:")
new_linked_list.traverse()

print("Is item present in the linked-list? ",new_linked_list.search(30))
print("Index of the item: ",new_linked_list.search_index(30))

print("Get the item using index (Here index is 3): ",new_linked_list.get(3).value)

print("This is head: ",new_linked_list.head.value)
print("This is tail: ",new_linked_list.tail.value)