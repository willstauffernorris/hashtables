
'''
## Day 2

Task: Implement linked-list chaining for collision resolution.

1. Modify `put()`, `get()`, and `delete()` methods to handle collisions.

2. There is no step 2.

You can test this with:

```
python test_hashtable.py
```

Task: Implement load factor measurements and automatic hashtable size
doubling.

1. Compute and maintain load factor.

2. When load factor increases above `0.7`, automatically rehash the
   table to double its previous size.

   Add the `resize()` method.

You can test this with both of:

```
python test_hashtable.py
python test_hashtable_resize.py
```

Stretch: When load factor decreases below `0.2`, automatically rehash
the table to half its previous size, down to a minimum of 8 slots.

'''

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        #self.hash_table = [None] * self.capacity
        self.hash_table = [None] * capacity
        self.num_items_in_hash = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here

        return len(self.hash_table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

        ## num of items passed in / num slots

        return self.num_items_in_hash/self.get_num_slots()




    # def fnv1(self, key):
    #     """
    #     FNV-1 Hash, 64-bit

    #     Implement this, and/or DJB2.
    #     """

    #     # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
            #hash = hash + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        !!!
        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # Your code here

        self.num_items_in_hash += 1
        
        new_hash_index = self.hash_index(key)
        # self.hash_list = HashTableEntry(new_hash_index, value)
        self.hash_table[new_hash_index] = value
        '''
        This is getting closer to the right logic for the linked list

        value_object = HashTableEntry(0, value)

        if self.hash_table[new_hash_index] == None:
            self.hash_table.insert(new_hash_index, value_object)
        else:
            print("COLLSION!")
            #self.hash_table[new_hash_index].next += 1
            #self.hash_table[new_hash_index]
        '''
        #rule of thumb: resize when the load factor is greater than .7
        if self.get_load_factor() > .7:
            self.resize(new_capacity=(self.capacity*2))

    

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        if key == None:
            print("KEY NOT FOUND")
            return
        new_hash_index = self.hash_index(key)
        self.hash_table.pop(new_hash_index)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        if key == None:
            print("KEY NOT FOUND")
            return None

        new_hash_index = self.hash_index(key)
        return self.hash_table[new_hash_index]



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        '''
        #rule of thumb: resize when the load factor is greater than .7
        self.capacity = new_capacity
        for item in self.hash_table:
            self.put(item.key, item.value)
        '''
        pass

        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    ht.put("key-3", "val-3")
    ht.put("key-4", "val-4")
    ht.put("key-5", "val-5")
    ht.put("key-6", "val-6")
    ht.put("key-7", "val-7")
    ht.put("key-8", "val-8")
    ht.put("key-9", "val-9")

    #return_value = ht.get("key-0")

    # print(ht.hash_table)
    print(ht.hash_table)
    print(ht.get_num_slots())
    print(ht.get_load_factor())


    #print(return_value)

    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_3", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    print("")
    #print(ht.djb2("dog"))
    # for item in ht.hash_table:
    #     print(item.value)

    #ht.delete("line_5")

    print("")

    # for item in ht.hash_table:
    #     print(item)

    #print(ht.get("line_8"))

    #print(ht.hash_table)

    #print(ht.hash_index("dog"))

    #print(ht.capacity)

    #print(ht.key)



    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    print("")
