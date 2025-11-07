class Bucket:
    def __init__(self, depth, size):
        self.depth = depth
        self.size = size
        self.keys = []
        self.values = []

    def is_full(self):
        return len(self.keys) >= self.size

    def insert(self, key, value):
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.values[i] = value
                return
        if not self.is_full():
            self.keys.append(key)
            self.values.append(value)

    def search(self, key):
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return self.values[i]
        return None

    def delete(self, key):
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.keys.pop(i)
                self.values.pop(i)
                return True
        return False

class ExtensibleHashTable:
    def __init__(self, bucket_size):
        self.global_depth = 1
        self.bucket_size = bucket_size
        self.directory = [Bucket(1, bucket_size) for _ in range(2)]

    def hash_function(self, key):
        return key % (2 ** self.global_depth)

    def double_directory(self):
        self.directory.extend(self.directory)
        self.global_depth += 1

    def split_bucket(self, index):
        old_bucket = self.directory[index]
        new_depth = old_bucket.depth + 1
        new_bucket = Bucket(new_depth, self.bucket_size)
        old_bucket.depth = new_depth
        if new_depth > self.global_depth:
            self.double_directory()
        for i in range(len(self.directory)):
            if i % (2 ** new_depth) >= 2 ** (new_depth - 1):
                self.directory[i] = new_bucket
        keys, values = old_bucket.keys[:], old_bucket.values[:]
        old_bucket.keys, old_bucket.values = [], []
        for i in range(len(keys)):
            self.insert(keys[i], values[i])

    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.directory[index]
        if bucket.is_full():
            self.split_bucket(index)
            self.insert(key, value)
        else:
            bucket.insert(key, value)

    def search(self, key):
        index = self.hash_function(key)
        return self.directory[index].search(key)

    def delete(self, key):
        index = self.hash_function(key)
        return self.directory[index].delete(key)

    def display(self):
        print(f"\nDirectory (Global Depth = {self.global_depth}):")
        seen = set()
        for i, bucket in enumerate(self.directory):
            if id(bucket) not in seen:
                seen.add(id(bucket))
                print(f"Index {i} (Depth {bucket.depth}):", list(zip(bucket.keys, bucket.values)))

def main():
    table = ExtensibleHashTable(bucket_size=2)
    while True:
        print("\n1. Insert\n2. Search\n3. Delete\n4. Display\n5. Exit")
        ch = input("Enter choice: ")
        if ch == '1':
            k = int(input("Enter key: "))
            v = input("Enter value: ")
            table.insert(k, v)
        elif ch == '2':
            k = int(input("Enter key: "))
            print("Value:", table.search(k))
        elif ch == '3':
            k = int(input("Enter key: "))
            print("Deleted" if table.delete(k) else "Not found")
        elif ch == '4':
            table.display()
        elif ch == '5':
            break
        else:
            print("Invalid choice!")

main()
