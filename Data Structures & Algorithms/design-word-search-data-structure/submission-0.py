class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        # curr pointer
        cur = self.root

        # add word to trie
        for char in word:
            # add to trie if letter not found
            if char not in cur.children:
                cur.children[char] = TrieNode()
            # update cur to char node
            cur = cur.children[char]

        # mark end of word
        cur.word = True
        

    def search(self, word: str) -> bool:
        def dfs(pos, root):     # cur position & curr root/node
            # current pointer = curr root/node
            cur = root

            # search word by chars
            for idx in range(pos, len(word)):
                char = word[idx]

                # dot case
                if char == ".":
                    # got through every children until match
                    for child in cur.children.values():
                        # if found a match
                        if dfs(idx + 1, child):
                            return True

                    return False

                # usual trie / search case
                else:
                    # check if char not in children
                    if char not in cur.children:
                        return False
                    # move cur to char node
                    cur = cur.children[char]
                    
            # return if a word 
            return cur.word
        
        # call dfs function
        return dfs(0, self.root)
