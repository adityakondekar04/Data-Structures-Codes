class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insertval(self.root, value)

    def insertval(self, node, value):
        if value < node.key:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insertval(node.left, value)
        elif value > node.key:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insertval(node.right, value)
        else:
            print("Value already exists in the BST.")

    def search(self, value):
        return self.searchval(self.root, value)

    def searchval(self, node, value):
        if node is None:
            return False
        if value == node.key:
            return True
        elif value < node.key:
            return self.searchval(node.left, value)
        else:
            return self.searchval(node.right, value)

    def delete(self, value):
        self.root = self.deleteval(self.root, value)

    def deleteval(self, node, value):
        if node is None:
            return None
        if value < node.key:
            node.left = self.deleteval(node.left, value)
        elif value > node.key:
            node.right = self.deleteval(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self.find_min(node.right)
            node.key = min_node.key
            node.right = self.deleteval(node.right, min_node.key)
        return node

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder(self):
        print("BST in sorted order:", end='')
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(f" {node.key}", end='')
            self._inorder(node.right)

    def display(self, node=None, level=0, label="Root:"):
        if node is None and level == 0:
            node = self.root
        if node is None:
            return
        print(' ' * (level * 4) + label + ' ' + str(node.key))
        if node.left is not None:
            self.display(node.left, level + 1, "L->")
        if node.right is not None:
            self.display(node.right, level + 1, "R->")


def run_bst_program():
    bst = BST()
    while True:
        print("\nBinary Search Tree Operations Menu:")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Inorder Traversal")
        print("5. Display Tree")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            value = int(input("Enter value to insert: "))
            bst.insert(value)
            print(f"Inserted {value} into the BST.")
        elif choice == '2':
            value = int(input("Enter value to search: "))
            found = bst.search(value)
            if found:
                print(f"Value {value} found in the BST.")
            else:
                print(f"Value {value} not found in the BST.")
        elif choice == '3':
            value = int(input("Enter value to delete: "))
            bst.delete(value)
            print(f"Deleted {value} from the BST (if it existed).")
        elif choice == '4':
            bst.inorder()
        elif choice == '5':
            if bst.root is not None:
                bst.display()
            else:
                print("The tree is empty.")
        elif choice == '6':
            print("Exiting the program.....\nProgram Exit Successful!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")



run_bst_program()
