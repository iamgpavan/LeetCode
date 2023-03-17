class Tries:
    def __init__(self):
        self.arr = dict()
        self.flag = False

    def contains(self, key):
        return key in self.arr

    def put(self, node, key):
        self.arr[key] = node

    def getNextNode(self, key):
        return self.arr[key]

    def setFlag(self):
        self.flag = True

    def getFlag(self):
        return self.flag

class Trie:

    def __init__(self):
        self.root = Tries()

    def insert(self, word: str) -> None:
        temp = self.root

        for i in word:
            if(not temp.contains(i)):
                newNode = Tries()
                temp.put(newNode, i)
            temp = temp.getNextNode(i)
        temp.setFlag()

    def search(self, word: str) -> bool:
        temp = self.root

        for i in word:
            if(not temp.contains(i)):
                return False
            temp = temp.getNextNode(i)

        return temp.getFlag()

    def startsWith(self, prefix: str) -> bool:
        temp = self.root

        for i in prefix:
            if(not temp.contains(i)):
                return False
            temp = temp.getNextNode(i)

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)