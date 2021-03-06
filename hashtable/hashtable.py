import sys

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    """
    Linked List structure to hold the elements that cause collision
    """
    def __init__(self):
        self.head = None

    def insert(self, node):
        cur = self.head
        if cur is None:
            self.head = node
        else:
        
            while cur is not None:
                if cur.key == node.key:
                    cur.value = node.value
                    break
                elif cur.next is None:
                    cur.next = node
                    break
                else:
                    cur = cur.next
    
    def find(self, key):
        cur = self.head
        while cur is not None:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return None
    
    def traverse(self):
        cur = self.head
        
        if cur is not None:
            self.head = self.head.next
           
            return cur
        return None
    
    def remove(self, key):
        cur = self.head
        prev = self.head
        if cur.key == key:
            self.head = self.head.next
            return cur
        prev =cur 
        cur = cur.next
        while cur is not None:
            if cur.key == key:
                return cur.value
            else:
                prev = prev.next
                cur = cur.next
        return None

MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.data = [None] * capacity
        self.capacity = capacity
        self.items = 0
       
    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        return len(self.data)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        return self.items/len(self.data)
        
    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """
        hval = 0x811c9dc5
        fnv_32_prime = 0x01000193
        uint32_max = 2 ** 32
        for s in key:
            hval = hval ^ ord(s)
            hval = (hval * fnv_32_prime) % uint32_max
        return hval

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % len(self.data)

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """       
        index = self.hash_index(key)
        if self.data[index] is None:
            ll = LinkedList()
            ll.insert(HashTableEntry(key, value))
            self.data[index] = ll
            self.items += 1
        else:
            self.data[index].insert(HashTableEntry(key, value))
            self.items += 1
        
        resize_factor = self.get_load_factor()
        if resize_factor >= 0.7:
            self.resize(len(self.data)*2)


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """    
        index = self.hash_index(key)
        removed = self.data[index].remove(key)
        
        if removed is not None:
            self.items -= 1
            return removed
        else:
            return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index1 = self.hash_index(key)
        if self.data[index1] is not None:
            return self.data[index1].find(key)
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        new_data = HashTable(new_capacity)

        for i in range(0, len(self.data)):
            if self.data[i] is not None: 
                while self.data[i].head is not None:
            
                    ll_node = self.data[i].traverse()
                
                    new_data.put(ll_node.key, ll_node.value)
        
        self.data = new_data.data

if __name__ == "__main__":
    ht = HashTable(8)
   
    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    print("")
   
    #Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    #Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    #Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")