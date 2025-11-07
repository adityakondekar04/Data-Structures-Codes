class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            temp = self.table[index]
            while temp.next:
                if temp.key == key:
                    temp.value = value
                    return
                temp = temp.next
            temp.next = new_node

    def search(self, key):
        index = self.hash_function(key)
        temp = self.table[index]
        while temp:
            if temp.key == key:
                print(f"Key {key} found with value '{temp.value}'.")
                return temp.value
            temp = temp.next
        print(f"Key {key} not found.")
        return None

    def delete(self, key):
        index = self.hash_function(key)
        temp = self.table[index]
        prev = None
        while temp:
            if temp.key == key:
                if prev:
                    prev.next = temp.next
                else:
                    self.table[index] = temp.next
                print(f"Key {key} deleted.")
                return
            prev = temp
            temp = temp.next
        print(f"Key {key} not found.")

    def display(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            temp = self.table[i]
            if not temp:
                print("Empty")
            else:
                while temp:
                    print(f"({temp.key}, {temp.value})", end=" -> ")
                    temp = temp.next
                print("None")

def main():
    htable = HashTable()
    while True:
        print("\n1. Insert\n2. Search\n3. Delete\n4. Display\n5. Exit")
        ch = input("Enter choice: ")
        if ch == '1':
            k = int(input("Enter key: "))
            v = input("Enter value: ")
            htable.insert(k, v)
        elif ch == '2':
            k = int(input("Enter key: "))
            htable.search(k)
        elif ch == '3':
            k = int(input("Enter key: "))
            htable.delete(k)
        elif ch == '4':
            htable.display()
        elif ch == '5':
            break
        else:
            print("Invalid choice!")

main()

