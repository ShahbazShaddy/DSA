print("\n\n-----------------------------------Part01 (b)--------------------------------------")
print("------------------------------------AVL Tree----------------------------------------")
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


print("\n\n-----------------------------------Part01 (a)--------------------------------------")
print("------------------------------------RB Tree--------------------------------------")
class Node:
    def __init__(self, key, color="RED"):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color="BLACK")  # Sentinel node representing NIL
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x

    def insert(self, key):
        new_node = Node(key)
        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y is None:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

        new_node.left = self.NIL
        new_node.right = self.NIL
        new_node.color = "RED"
        self.insert_fixup(new_node)

    def insert_fixup(self, node):
        while node.parent is not None and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == "RED":
                    node.parent.color = "BLACK"
                    y.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.color == "RED":
                    node.parent.color = "BLACK"
                    y.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)

        self.root.color = "BLACK"

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent

    def delete(self, key):
        z = self.search(key)
        if z is None:
            print("Node with key {} not found.".format(key))
            return

        y = z
        y_original_color = y.color

        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == "BLACK":
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = "BLACK"

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or key == node.key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x

    def inorder_traversal(self, node):
        if node != self.NIL:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)


# Example usage:
rb_tree = RedBlackTree()
keys = [10, 20, 30, 15, 25, 5]

for key in keys:
    rb_tree.insert(key)

print("Inorder traversal after insertion:")
rb_tree.inorder_traversal(rb_tree.root)

key_to_delete = 20
rb_tree.delete(key_to_delete)

print("\nInorder traversal after deleting", key_to_delete, ":")
rb_tree.inorder_traversal(rb_tree.root)



