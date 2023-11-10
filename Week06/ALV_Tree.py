class AVLNode:
    def __init__(self, val):
        self.val = val
        self.height = 1
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return 0
    return node.height


def update_height(node):
    if node is not None:
        node.height = 1 + max(height(node.left), height(node.right))


def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)


def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    update_height(y)
    update_height(x)

    return x


def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    update_height(x)
    update_height(y)

    return y


def insert(root, val):
    if root is None:
        return AVLNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    # Update height of the current node
    update_height(root)

    # Perform balancing
    return balance(root)


def delete_node(root, val):
    if root is None:
        return root

    if val < root.val:
        root.left = delete_node(root.left, val)
    elif val > root.val:
        root.right = delete_node(root.right, val)
    else:
        # Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Node with two children: Get the in-order successor (smallest
        # in the right subtree) or predecessor (largest in the left subtree)
        successor = find_min(root.right)
        root.val = successor.val
        root.right = delete_node(root.right, successor.val)

    # Update height of the current node
    update_height(root)

    # Perform balancing
    return balance(root)


def balance(node):
    if node is None:
        return node

    # Left Heavy
    if balance_factor(node) > 1:
        if balance_factor(node.left) < 0:
            # Left-Right case
            node.left = left_rotate(node.left)
        # Left-Left case
        return right_rotate(node)

    # Right Heavy
    if balance_factor(node) < -1:
        if balance_factor(node.right) > 0:
            # Right-Left case
            node.right = right_rotate(node.right)
        # Right-Right case
        return left_rotate(node)

    return node


def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)


# Example usage:
root = None
values = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for value in values:
    root = insert(root, value)

print("Inorder traversal after insertion:")
inorder_traversal(root)

value_to_delete = 10
root = delete_node(root, value_to_delete)

print("\nInorder traversal after deleting", value_to_delete, ":")
inorder_traversal(root)
