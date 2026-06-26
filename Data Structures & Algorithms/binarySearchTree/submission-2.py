class TreeNode:
    # initialize class
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:

    def __init__(self):
        # Initialize node
        self.root = None

    def insert(self, key: int, val: int) -> None:
        # if list is empty, insert at root
        if not self.root:
            self.root = TreeNode(key, val)
            return

        # intialize new map
        new_node = TreeNode(key, val)
        # call function to insert pair
        self.insert_bst(self.root, new_node)

    # insert key to tree through bst
    def insert_bst(self, root, new_node):
        # if not found
        if not root:
            return new_node
        # check if target-key less than curr-key
        if new_node.key < root.key:
            root.left = self.insert_bst(root.left, new_node)
        # check if target-key grater than curr-key
        elif new_node.key > root.key:
            root.right = self.insert_bst(root.right, new_node)
        else:
            root.key = new_node.key
            root.val = new_node.val
        #return/update new tree
        return root



    def get(self, key: int) -> int:
        #bst key function
        def get_bst(root, target):
            # if target key not found
            if not root:
                return -1

            # check if less than curr key
            if target < root.key:
                return get_bst(root.left, target)
            # check if target key less than curr key
            elif target > root.key:
                return get_bst(root.right, target)
            # if target key found
            else:
                return root.val

        # call bst function
        res = get_bst(self.root, key)

        # return result
        return res



    def getMin(self) -> int:
        if not self.root:
            return -1

        # DFS for min val
        curr = self.root
        while curr.left:
            curr = curr.left

        #return min val
        return curr.val


    def getMax(self) -> int:
        if not self.root:
            return -1

        # DFS for max val
        curr = self.root
        while curr.right:
            curr = curr.right

        #return min val
        return curr.val

    def remove(self, key: int) -> None:
        # BST to find val
        self.root = self.help_remove(self.root, key)


    def help_remove(self, root, key):
        # if not found return tree
        if not root:
            return root

        # key is less than curr key so traverse less
        if key < root.key:
            root.left = self.help_remove(root.left, key)
        # key is greater than curr key so traverse right
        elif key > root.key:
            root.right = self.help_remove(root.right, key)

        # node found
        else:
            # if only left
            if not root.right:
                return root.left
            # if only right
            elif not root.left:
                return root.right

            else:
                #check children of right mode
                curr = root.right

                while curr.left:
                    curr = curr.left

                #update target node key/val with grabbed key/val
                root.key = curr.key
                root.val = curr.val

                #delete grabbed node 
                root.right = self.help_remove(root.right, curr.key)
        # return updated tree
        return root


    def getInorderKeys(self) -> List[int]:
        # list to store keys
        keys = []
        # call function to add keys
        self.inorder(self.root, keys)
        # return keys
        return keys

    # recursion DFS to store keys inorder
    def inorder(self, root, res):
        if not root:
            return
        # traverse left until end
        self.inorder(root.left, res)
        # add key to list
        res.append(root.key)
        # traverse right until end
        self.inorder(root.right, res)

