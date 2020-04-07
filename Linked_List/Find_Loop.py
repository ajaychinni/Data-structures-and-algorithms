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
        
    def create_loop(self,start,end):
        cur_node1 = self.head
        while cur_node1 and cur_node1.data is not start:
            cur_node1 = cur_node1.next
        
        cur_node2  = self.head
        while cur_node2 and cur_node2.data is not end:
            cur_node2 = cur_node2.next
            
        # creating a loop between end and start 
        cur_node2.next = cur_node1
        
    def find_loop(self):
        d = {}
        cur_node = self.head
        while cur_node:
            if cur_node.next in d:
                return True
            else:
                d[cur_node.next] = 1
            cur_node = cur_node.next
        return False
                
    def display(self):
        last_node = self.head
        while last_node:
            print(last_node.data)
            last_node = last_node.next
    
ll = Linked_list()
ll.add(1)
ll.add(2)
ll.add(3)
ll.create_loop(1,2)
print(ll.find_loop())
# ll.display()