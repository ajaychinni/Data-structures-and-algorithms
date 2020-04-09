class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linked_list:
    def __init__(self):
        self.head = None
        
    def add(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
            
        cur_node  = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
        
    def display(self):
        last_node = self.head
        while last_node:
            print(last_node.data)
            last_node = last_node.next
    
        
    def rev(self):
        cur_node = self.head
        prev = None
        while cur_node:
            nxt = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = nxt 
        self.head = prev
            
        
        
        
ll = Linked_list()
ll.add(1)
ll.add(2)
ll.add(3)
ll.rev()
ll.display()