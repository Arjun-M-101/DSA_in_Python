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
    
    def set_value (self,value,index):
        if index < -1 or index >= self.length:
            return False
        if index == -1:
            self.tail.value = value
            return self.tail
        current = self.head
        for _ in range(index):
            current = current.next
        if current:
            current.value = value
            return current
        else:
            return False
    
    def set_by_get (self,value,index):
        temp = self.get(index)
        if temp:
            temp.value = value
            return temp
        else:
            return False
        
    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            popped_node = self.head
            self.head = popped_node.next
            popped_node.next = None
        self.length -=1
        return popped_node
    
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            popped_node = self.tail
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node
        
    def remove(self,index):
        if index < -1 or index >= self.length:
            return False
        if self.length == 0:
            return None
        # if self.length == 1:  #ALREADY PRESENT IN POP METHODS
        #     self.head = None
        #     self.tail = None
        #     return self.head
        if index == self.length-1 or index == -1:
            return self.pop()
        elif index == 0:
            return self.pop_first()
        else:
            pre = self.get(index-1)
            popped_node = pre.next
            pre.next = popped_node.next
            popped_node.next = None
            self.length -= 1
            #                         VALIDATION AFTER REMOVAL - NOT REQUIRED
            # if self.length == 0:   #ALREADY PRESENT IN POP METHODS
            #     return None
            # if self.length == 1:
            #     self.head = None
            #     self.tail = None
            #     return self.head
            return popped_node
        
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
        
new_linked_list = LinkedList()

print("Initial linked_list: ",new_linked_list.head,"\n")

new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
new_linked_list.append(50)
print("Appending items, 10, 20, 30, 40, 50: ")
print(new_linked_list,"\n")

print("Inserting item 0 at index 0: ")
new_linked_list.insert(0,0)
print(new_linked_list,"\n")

print("Inserting item 60 at index 6: ")
new_linked_list.insert(60,6)
print(new_linked_list,"\n")

print("Traversing inside the linked-list:")
new_linked_list.traverse()
print("")

print("Is item (30) present in the linked-list? ",new_linked_list.search(30))
print("Index of the item: ",new_linked_list.search_index(30),"\n")

print("Get the item using index (Here index is 3): ",new_linked_list.get(3).value,"\n")

print("Set value to the item using index (Here index is 4 & value is 45): ")
new_linked_list.set_value(65,-1)
print(new_linked_list)
print("Set value to the item using index (Here index is 5 & value is 55): ")
new_linked_list.set_by_get(55,5)
print(new_linked_list,"\n")

print("Pop the first item: ",new_linked_list.pop_first().value)
print(new_linked_list,"\n")

print("Pop the last item: ",new_linked_list.pop().value)
print(new_linked_list,"\n")

print("Removed item: ",new_linked_list.remove(-1).value)
print(new_linked_list,"\n")

# print("Delete all items in linked-list: ")
# new_linked_list.delete_all()
# print(new_linked_list,"\n")

print("Reverse linked-list: ")
new_linked_list.reverse()
print(new_linked_list,"\n")

print("Traversing inside the linked-list:")
new_linked_list.traverse()
print("")

'''ADD YOUR PRINT STATEMENTS BELOW THIS'''



''' 
**** DO NOT REMOVE THE BELOW LINES ***
'''
try:
    print("LINKED-LIST:",new_linked_list)
    print("This is head: ",new_linked_list.head.value)
    print("This is tail: ",new_linked_list.tail.value)
    print("Length of the linked-list is: ",new_linked_list.length)
except Exception:
    print("(Invalid linked-list)")