
'''
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

        ## linked list

        new_node = HashTableEntry(key, value)
        #print(new_node.key)
        #print(new_node.next)

        new_hash_index = self.hash_index(key)

        if self.hash_table[new_hash_index] is None:
            self.hash_table[new_hash_index] = new_node
            #print(self.hash_table[new_hash_index])
            # print(self.hash_table[new_hash_index].key)
            # print(self.hash_table[new_hash_index].value)
            # print(self.hash_table[new_hash_index].next)
            #print(self.hash_table)

        #if something is in that slot
        elif self.hash_table[new_hash_index] is not None:
            # print("COLLISION")
            # print(f'current node {self.hash_table[new_hash_index].value}')
            # print(f'current .next {self.hash_table[new_hash_index].next}')

            #replace the current index with this new one
            old_node = self.hash_table[new_hash_index]
            self.hash_table[new_hash_index] = new_node
            # print(f'new current node {self.hash_table[new_hash_index].value}')
            self.hash_table[new_hash_index].next = old_node
            # print(f'new .next {self.hash_table[new_hash_index].next.value}')


        ## need logic to overwrite a value with the same key
        # if the key exists, update value
        # if it doesn't exist, make a new node


        # self.hash_list = HashTableEntry(new_hash_index, value)
        #self.hash_table[new_hash_index] = value
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

#         Stretch: When load factor decreases below `0.2`, automatically rehash
# the table to half its previous size, down to a minimum of 8 slots.'

        # if self.get_load_factor() < .2:
        #     self.resize(new_capacity = (self.capacity//2))



    

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
        current_node = self.hash_table[new_hash_index]
        next_node = current_node.next

        #print(current_node.key)
        #print(next_node.key)


        previous_node = None

        while current_node.key != key:
            if current_node.next == None:
                print("THERE IS NO NEXT")
                return None
            else:
                previous_node = current_node
                current_node = current_node.next

        if previous_node == None:
            self.hash_table[new_hash_index] = current_node.next
        else:
            previous_node.next = current_node.next
                
            
    


        # if current_node.next == None:
        #     print("REMOVING ELEMENT FROM HASH TABLE")
        #     current_node=None
        # ## if it's a collison:
        # else:  
        #     print("DELETE COLLISION")
        
        #     current_node=current_node.next
            # while current_node.next is not None:
            #     if current_node.key == key:
            #         print("DELETING")
            #         current_node = current_node.next
            #     current_node = current_node.next
            
        

            # if current_node.key == key:
            #     print("DELETING IT")
            #         #print(current_node.value)
            #     current_node = current_node.next
            #     print(current_node)


            # while current_node.next is not None:
            #     print(current_node.key)
            #     next_node = current_node.next
            #     print(f'NEXT {next_node.key}')
            #     ## compare
            #     #  with original key
            #     # if key matches, return original value
            #     if current_node.key == key:
            #         print("DELETING IT")
            #         #print(current_node.value)
            #         current_node = current_node.next
            #         print(current_node)
            #     # if not found, return None
            #     # else:
            #     #     print("COULDN'T FIND IT")
            #     #     return None
            #     #print(f'CURRENT Node {current_node}')
            #     current_node = current_node.next
            #     print(f'CURRENT Node {current_node.key}')
            #     print(f'NEXT Node {current_node.next}')
            
            
            # print("REMOVING ELEMENT FROM HASH TABLE")
            # current_node = current_node.next


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # if key == None:
        #     print("KEY NOT FOUND")
        #     return None

        new_hash_index = self.hash_index(key)
        # return self.hash_table[new_hash_index]

        if self.hash_table[new_hash_index] == None:
            #print("KEY NOT FOUND")
            return None


        current_next = self.hash_table[new_hash_index].next
        current_node = self.hash_table[new_hash_index]



        if current_next == None:
            if current_node.key == key:
                return self.hash_table[new_hash_index].value
            else: 
                return None
        ## if it's a collison:
        else:        
            #print("COLLISION")
            while current_next is not None:
                ## compare with original key
                # if key matches, return original value
                if current_node.key == key:
                    #print("FOUND IT")
                    #print(current_node.value)
                    return current_node.value
                # if not found, return None
                # else:
                #     print("COULDN'T FIND IT")
                #     return None
                #print(f'CURRENT Node {current_node}')
                current_node = current_node.next
                #print(f'CURRENT Node {current_node}')
        
        
        
        

        # #current = self.head
        # current = self.hash_table[new_hash_index]
        # while current is not None:
        #     if current.key == key:
        #         return current
            
        #     current = current.next



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        
        #rule of thumb: resize when the load factor is greater than .7
        self.capacity = new_capacity

        #saving the old hash table
        old_hash_table = self.hash_table

        #creating a new hash table with bigger capacity
        self.hash_table = [None] * self.capacity

        for item in old_hash_table:
            if item.next == None:
                self.put(item.key, item.value)
            else:
                while item.next is not None:
                    self.put(item.key, item.value)
                    item = item.next
                self.put(item.key, item.value)




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

    # for item in ht.hash_table:
    #     print(item.value)
    #     print(item.next)
    return_value = ht.get("key-0")
    print(return_value)

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


    print("")


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
