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
    
tree = BinarySearchTree()
for v in [7, 3, 9, 1, 5, 8, 10]:
    tree.insert(v)

print(tree.inorder())
print(tree.preorder())
print(tree.postorder())
    