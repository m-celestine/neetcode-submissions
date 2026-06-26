class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        # init cur at root
        cur = self.root
        # add word to Trie/root
        for char in word:
            # add unseen chars to map
            if char not in cur.children:
                # init char as a node in map
                cur.children[char] = TrieNode()
            # move cur to next(char) node
            cur = cur.children[char]
        # mark end of a word
        cur.word = True



    def search(self, word: str) -> bool:
        # init cur at root
        cur = self.root
        # check if word/chars in Trie
        for char in word:
            # check if char in Trie
            if char not in cur.children:
                return False
            # move to next char 
            cur = cur.children[char]
        # return if word if found
        return cur.word
        

    def startsWith(self, prefix: str) -> bool:
        # init cur at root
        cur = self.root
        # check if word/chars in Trie
        for char in prefix:
            # check if char in Trie
            if char not in cur.children:
                return False
            # move to next char 
            cur = cur.children[char]
        # return chars found
        return True
        
        