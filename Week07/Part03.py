class KeyNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MyHashTable:
    def __init__(self, hsize):
        self.array = [None] * hsize
        self.size = hsize
        self.keys_occupied = 0

    def get_hash_table_size(self):
        return self.size

    def get_number_of_keys(self):
        return self.keys_occupied

    def hash_function(self, key):
        # Simple hash function: sum of ASCII values modulo table size
        return sum(ord(char) for char in key) % self.size

    def update_key(self, key, value):
        index = self.hash_function(key)
        if self.array[index] is None:
            self.array[index] = [KeyNode(key, value)]
            self.keys_occupied += 1
        else:
            # Check if key already exists in the list
            for node in self.array[index]:
                if node.key == key:
                    node.value += value
                    return
            # If key not found in the list, add a new KeyNode
            self.array[index].append(KeyNode(key, value))
            self.keys_occupied += 1

        # Check if rehashing is needed
        if self.keys_occupied > 2 * self.size:
            self.rehash()

    def search_key(self, key):
        index = self.hash_function(key)
        if self.array[index] is not None:
            for node in self.array[index]:
                if node.key == key:
                    return node.value
        return 0  # Key not found

    def rehash(self):
        new_size = 2 * self.size
        new_array = [None] * new_size

        # Rehashing: iterate through the old array and redistribute nodes to the new array
        for bucket in self.array:
            if bucket is not None:
                for node in bucket:
                    new_index = sum(ord(char) for char in node.key) % new_size
                    if new_array[new_index] is None:
                        new_array[new_index] = [node]
                    else:
                        new_array[new_index].append(node)

        self.array = new_array
        self.size = new_size


# Function to count word occurrences in a text file
def count_word_occurrences(filename):
    hash_table = MyHashTable(128)

    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            hash_table.update_key(word, 1)

    # Output word occurrences
    for index in range(hash_table.get_hash_table_size()):
        if hash_table.array[index] is not None:
            for node in hash_table.array[index]:
                print(f"{node.key} {node.value}")


# Example usage:
count_word_occurrences("example.txt")
