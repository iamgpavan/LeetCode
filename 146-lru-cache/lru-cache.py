class Node:
    def __init__(self, key, data):
        self.prev = None
        self.data = data
        self.key = key
        self.next = None

class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self, cap):
        #code here
        self.cap = cap
        self.head = None
        self.tail = None
        self.hm = {}
        
    def move_to_tail(self, node):
        if(node == None or node==self.tail):
            return
    
        if(node == self.head and self.tail != self.head):
            self.head = self.head.next
        
        if(node.prev):
            node.prev.next = node.next
        if(node.next):
            node.next.prev = node.prev
        
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

       
        
    def insert_at_tail(self, node):
        if(self.head == None):
            self.head = node
            self.tail = node
        else: 
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        if(key in self.hm):
            node = self.hm[key]
            self.move_to_tail(node)
            return node.data
        return -1
    
    def llPrinter(self):
        temp = self.head
        
        while(temp != None):
            print(temp.key, temp.data, end="->")
            temp = temp.next
        
    #Function for storing key-value pair.   
    def put(self, key, value):
        #code here
        if(key in self.hm):
            node = self.hm[key]
            node.data = value
            self.move_to_tail(node)
        else:
            node = Node(key, value)
            
            self.hm[key] = node
            self.insert_at_tail(node)
            if(len(self.hm) > self.cap):
                removed = self.head.key
                del self.hm[removed]
                self.head = self.head.next
        #         print("del value", removed, self.hm)
        # print()
        # self.llPrinter()
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)