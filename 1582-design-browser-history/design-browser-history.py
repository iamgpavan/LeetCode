class Node:
    def __init__(self, val = "", prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr = self.head
        # self.hm = {homepage:self.head}

    def visit(self, url: str) -> None:
        # if url not in self.hm:
        newNode = Node(url)
        newNode.prev = self.curr
        self.curr.next = newNode
        self.curr = self.curr.next
        # self.hm[url] = newNode
        # print(self.curr.val)
        # else:
        #     self.curr = self.hm[url]
        #     self.curr.next = None

    def back(self, steps: int) -> str:
        # if(self.curr == self.head):
        #     return ""
        while(steps and self.curr.prev != None):
            self.curr = self.curr.prev
            steps -= 1
        
        return self.curr.val

    def forward(self, steps: int) -> str:
        while(steps and self.curr.next != None):
            self.curr = self.curr.next
            steps -= 1
        
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)