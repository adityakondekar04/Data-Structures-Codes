class Node:
    def __init__(self, city, population):
        self.city = city
        self.population = population
        self.left = None
        self.right = None

class CityBST:
    def __init__(self):
        self.root = None

    def add_city(self, city, population):
        self.root = self.insert(self.root, city, population)

    def insert(self, node, city, population):
        if node is None:
            return Node(city, population)
        if city < node.city:
            node.left = self.insert(node.left, city, population)
        elif city > node.city:
            node.right = self.insert(node.right, city, population)
        else:
            node.population = population
        return node

    def delete_city(self, city):
        self.root = self.delete(self.root, city)

    def delete(self, node, city):
        if node is None:
            return None
        if city < node.city:
            node.left = self.delete(node.left, city)
        elif city > node.city:
            node.right = self.delete(node.right, city)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self.min_value_node(node.right)
            node.city = min_node.city
            node.population = min_node.population
            node.right = self.delete(node.right, min_node.city)
        return node

    def min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def update_population(self, city, population):
        node = self.search(self.root, city)
        if node is not None:
            node.population = population
            print(f"Updated {city} to population {population}.")
        else:
            print(f"{city} not found.")

    def search(self, node, city):
        if node is None or node.city == city:
            return node
        if city < node.city:
            return self.search(node.left, city)
        else:
            return self.search(node.right, city)

    def display(self, ascending=True):
        if ascending:
            self.inorder(self.root)
        else:
            self.reverse_inorder(self.root)

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(f"{node.city} - {node.population}")
            self.inorder(node.right)

    def reverse_inorder(self, node):
        if node is not None:
            self.reverse_inorder(node.right)
            print(f"{node.city} - {node.population}")
            self.reverse_inorder(node.left)

    def max_comparisons_to_search(self):
        return self.height(self.root)

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

bst = CityBST()
bst.add_city("Pune", 2500000)
bst.add_city("Mumbai", 30000000)
bst.add_city("Kolhapur", 1000000)
bst.add_city("Solapur", 2200000)

print("\nCities in ascending order:")
bst.display(True)
print("\nCities in descending order:")
bst.display(False)

bst.update_population("Pune", 3600000)
bst.delete_city("Nashik")

print("\nAfter updates:")
bst.display(True)
print("\nMaximum comparisons to search:", bst.max_comparisons_to_search())
