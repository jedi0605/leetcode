class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.node
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True        

    def search(self, word: str) -> bool:
        cur = self.node
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]             
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.node
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]             
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)