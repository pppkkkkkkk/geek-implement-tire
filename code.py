class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

#User function Template for python3
class Trie:
    def __init__(self):
        # implement Trie
        self.root = TrieNode()
        
    def insert(self, word: str):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
         curr = self.root
         for char in word:
             if char not in curr.children:
                 return False
             curr = curr.children[char]
         return curr.endOfWord

    def isPrefix(self, word: str) -> bool:
         # search prefix word in the Trie
         curr = self.root
         for char in word:
             if char not in curr.children:
                 return False
             curr = curr.children[char]
         return True
         