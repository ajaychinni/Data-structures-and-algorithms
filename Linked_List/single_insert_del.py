class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkdedList:
    def __init__(self):
        self.head = None
    
    def add(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node
    
    def display(self):
        last_node = self.head
        while last_node:
            print(last_node.data)
            last_node = last_node.next
    
    def search(self,k):
        last_node = self.head
        while last_node:
            if last_node.data == k:
                return True
            last_node = last_node.next
        return False
        
    def remove(self,k):
        if self.head is None:
            return  
        #if k is head
        if self.head and self.head.data == k:
            self.head = self.head.next
            return
        
        curr_node = self.head
        prev = None
        while curr_node.data != k:
            prev = curr_node
            curr_node = curr_node.next
        if curr_node.data == k:
            prev.next = curr_node.next
        return
    
    def swap(self,data1,data2):
        cur_node1 = self.head
        prev1 = None
        while cur_node1.data != data1:
            prev1 = cur_node1
            cur_node1 = cur_node1.next
        
        cur_node2 = self.head
        prev2 = None
        while cur_node2.data != data2:
            prev2 = cur_node2
            cur_node2 = cur_node2.next
        
        
        if prev1:
            prev1.next = cur_node2
        else:
            self.head = cur_node2
        if prev2:
            prev2.next = cur_node1
        else:
            self.head = cur_node1
        cur_node1.next, cur_node2.next = cur_node2.next, cur_node1.next

        
        
ll = LinkdedList()
ll.add("A")
ll.add("B")
ll.add("C")
ll.add("D")
ll.swap("A","B")
# ll.remove("A")
# print(ll.search("A"))
ll.display()