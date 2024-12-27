class Node:
   def __init__(self, key):
       self.left = None
       self.right = None
       self.val = key

# Функция для добавления нового узла
def insert(root, key):
   if root is None:
       return Node(key)
   else:
       if root.val < key:
           root.right = insert(root.right, key)
       else:
           root.left = insert(root.left, key)
   return root



# Пример использования
root = Node(70)
root = insert(root, 30)
root = insert(root, 56)
root = insert(root, 89)
root = insert(root, 45)
root = insert(root, 60)
root = insert(root, 73)
root = insert(root, 98)
root = insert(root, 84)

# Функция для in-order обхода дерева
def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.val, end=" ")  # Печать значения узла
        inorder_traversal(root.right)

# Вызов in-order обхода
inorder_traversal(root)

# Функция для визуализации дерева
def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.val))
        print_tree(node.left, level + 1, "L--- ")
        print_tree(node.right, level + 1, "R--- ")

# Вызов функции печати
print_tree(root)