class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
                root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete_node(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        # Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.val = find_min(root.right).val
        root.right = delete_node(root.right, root.val)
    return root

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.right)
        print(root.val, end=" ")
        inorder_traversal(root.left)

def preoder_traversal(root):
    if root is not None:
        print(root.val, end=" ")
        preoder_traversal(root.right)
        preoder_traversal(root.left)
def postorder_traversal(root):
    if root is not None:
        postorder_traversal(root.right)
        postorder_traversal(root.left)
        print(root.val, end=" ")
root = None
keys=[5, 1, 9, 3, 7, 2, 8, 4, 6]
for key in keys:
    root = insert(root, key)

preoder_traversal(root)
print(" ")
inorder_traversal(root)
print(" ")
postorder_traversal(root)
print(" ")
print(" ")

key_to_delete = 8
root=delete_node(root,key_to_delete)
print("After Deleting\n")
preoder_traversal(root)
print(" ")
inorder_traversal(root)
print(" ")
postorder_traversal(root)

