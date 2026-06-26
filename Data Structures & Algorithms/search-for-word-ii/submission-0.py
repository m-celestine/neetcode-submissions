class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode() 
            cur = cur.children[char]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # init root node
        root = TrieNode()

        # add words to Trie
        for w in words:
            root.addWord(w)

        # init Rows and Cols
        Rows, Cols = len(board), len(board[0])

        # init res and visited as sets
        res, visited = set(), set()


        def dfs(row, col, node, word):
            # edge case
            if (row < 0 or col < 0 or row >= Rows or col >= Cols or (row, col) in visited or board[row][col] not in node.children):
                return

            # add and traverse
            visited.add((row, col))
            # update node to cur node
            node = node.children[board[row][col]]
            # add letter to word
            word += board[row][col]

            # add to results if valid/completed word
            if node.isWord:
                res.add(word)


            # check surrounding letters
            dfs(row + 1, col, node, word)
            dfs(row - 1, col, node, word)
            dfs(row, col + 1, node, word)
            dfs(row, col - 1, node, word)

            #remove from visited
            visited.remove((row, col))


        # find words throughout board
        for r in range(Rows):
            for c in range(Cols):
                dfs(r, c, root, "")

        # return words
        return list(res)