"""Binary tree traversals: preorder, inorder and postorder."""

# A class that represents an individual node in a
# Binary Tree


class Node:
    """A binary tree node holding a value and left/right children."""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def print_inorder(root):
    """Prints values in left, root, right order."""
    if root:
        # First recur on left child
        print_inorder(root.left)

        # then print the data of node
        print(root.val)

        # now recur on right child
        print_inorder(root.right)


# A function to do postorder tree traversal
def print_postorder(root):
    """Prints values in left, right, root order."""
    if root:
        # First recur on left child
        print_postorder(root.left)

        # the recur on right child
        print_postorder(root.right)

        # now print the data of node
        print(root.val)


# A function to do preorder tree traversal
def print_preorder(root):
    """Prints values in root, left, right order."""
    if root:
        # First print the data of node
        print(root.val)

        # Then recur on left child
        print_preorder(root.left)

        # Finally recur on right child
        print_preorder(root.right)


def main():
    """Builds a sample tree and prints all three traversals."""
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    print("Preorder traversal of binary tree is")
    print_preorder(tree)

    print("\nInorder traversal of binary tree is")
    print_inorder(tree)

    print("\nPostorder traversal of binary tree is")
    print_postorder(tree)


if __name__ == "__main__":
    main()
