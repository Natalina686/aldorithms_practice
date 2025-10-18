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
    
    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if not node.left and not node.right:
                return None
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            min_larger_node = node.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left
            node.value = min_larger_node.value
            node.right = self._delete(node.right, min_larger_node.value)
        return node
    
    def count_nodes(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        if not node:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)
    
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if not node:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return 1 + max(left_height, right_height)
    
    def is_bst(self):
        return self._is_bst(self.root, float('-inf'), float('inf'))

    def _is_bst(self, node, min_val, max_val):
        if not node:
            return True
        if not (min_val < node.value < max_val):
            return False
        return (self._is_bst(node.left, min_val, node.value) and
            self._is_bst(node.right, node.value, max_val))



        

    
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
tree.delete(7)
print(tree.inorder())
print("Nodes:", tree.count_nodes())
print("Height:", tree.height())
print("Is BST?", tree.is_bst())

tree.delete(5)
print("Nodes after deletion:", tree.count_nodes())
print("Height after deletion:", tree.height())
print("Is BST after deletion?", tree.is_bst()) 
    