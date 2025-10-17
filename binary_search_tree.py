class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = Node(value)

    def inorder(self):
        return self._inorder(self.root, [])
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)
        return result
    
    def preorder(self):
        return self._preorder(self.root, [])
    
    def _preorder(self, node, result):
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
        return result
    
    def postorder(self):
        return self._postorder(self.root, [])
    
    def _postorder(self, node, result):
        if node:
            
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)
        return result
    
    def find(self, value):
        return self._find(self.root, value)
    
    def _find(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._find(node.left, value)
        else:
            return self._find(node.right, value)
        
    def find_min(self):
        node = self.root
        if not node:
            return None
        while node.left:
            node = node.left
        return node.value
    
    def find_max(self):
        node = self.root
        if not node:
            return None
        while node.right:
            node = node.right
        return node.value
        

    
tree = BinarySearchTree()
for v in [7, 3, 9, 1, 5, 8, 10]:
    tree.insert(v)

print(tree.inorder())
print(tree.preorder())
print(tree.postorder())
print(tree.find_min())
print(tree.find_max())
print(tree.find(20))
print(tree.find(5))
    