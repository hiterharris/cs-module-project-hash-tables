class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.storage = [None] * capacity  # [None, None, None...]
        self.size = 0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function
        Implement this, and/or DJB2.
        """
        hash = 14695981039346656037
        prime = 1099511628211

        key_bytes = key.encode()

        for byte in key_bytes:
            hash ^= byte
            hash *= prime
        return hash

    def djb2(self, key):
        """
        DJB2 32-bit hash function
        Implement this, and/or FNV-1.
        """

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        index = self.hash_index(key)
        entry = HashTableEntry(key, value)
        if self.storage[index] is None:
            self.size += 1
            self.storage[index] = entry
            self.resize()
            return
        node = self.storage[index]
        while node.next is not None and node.key != key:
            node = node.next
        if node.key == key:
            node.value = value
            return
        self.size += 1
        node.next = entry
        self.resize()


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]
        if node is None:
            return
        previous_node = None
        while node is not None:
            if node.key == key:
                if previous_node is None:
                    self.storage[index] = node.next
                    self.size -= 1
                    return
                else:
                    previous_node.next = node.next
                    self.size -= 1
                    return
            else:
                previous_node = node
                node = node.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is None:
            return None
        node = self.storage[index]
        while node.key != key:
            if node.next is None:
                return None
            node = node.next
        return node.value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Implement this.
        """
        if self.size / self.capacity <= 0.7:
            return
        actual_size = self.size
        self.capacity *= 2
        old_storage = self.storage.copy()
        self.storage = [None] * self.capacity
        for node in old_storage:
            if node is None:
                continue
            while node.next is not None:
                self.put(node.key, node.value)
                node = node.next
            self.put(node.key, node.value)
            self.size = actual_size

if __name__ == "__main__":

    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")
    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")