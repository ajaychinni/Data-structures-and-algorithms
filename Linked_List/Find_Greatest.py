class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linked_list:
    def __init__(self):
        self.head  = None
        
    def add(self,data):
        new_node  = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        cur_node  = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
        
        
    def find_gratest(self):
        maxs = self.head.data
        cur_node = self.head
        while cur_node:
            if cur_node.data > maxs:
                maxs = cur_node.data
            cur_node = cur_node.next
        return maxs         
        
ll  = Linked_list()
ll.add(1)
ll.add(3)
ll.add(2)
ll.add(6)
print(ll.find_gratest())
        
                