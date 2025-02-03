class TrieNode:
    def __init__(self):
        self.maps = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.maps:
                cur.maps[w] = TrieNode()
            cur = cur.maps[w]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.maps:
                return False
            cur = cur.maps[w]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w not in cur.maps:
                return False
            cur = cur.maps[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
