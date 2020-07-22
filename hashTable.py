# my custom hash table class

# TODO big o notation
class MyHashTable:
    # the constructor. It will have the initial capacity of the hash table as parameter
    def __init__(self, capacity):
        # creates an empty buckets list.
        self.hash_list = []
        # creates an empty list for each bucket to handle collisions
        for bucket in range(capacity):
            self.hash_list.append([])

    # this method contains the hash function.
    # it will be used to determine to which bucket each item will go
    # it has a big O notation of O(1)
    def _my_hash(self,key):
        index = int(key) % len(self.hash_list)
        print("modulo de ", len(self.hash_list))
        print("index no my have: ", index)
        return index

    # to add the key and value into the hash table
    # it has a big O notation of O(1)
    def add(self,key,value):
        bucket_index = self._my_hash(key)
        print("bucket index no add, should be the same as id: ", bucket_index)
        item_to_add = [key, value]
        # selected_bucket is the bucket selected by the hash function
        selected_bucket = self.hash_list[bucket_index]
        # Since each bucket has a list, it will append the key and value to the bucket list
        selected_bucket.append(item_to_add)
        print("selected bucket no index",bucket_index,"item", selected_bucket)

    # to search for a key
    # it has a big O notation of O(n)
    def search(self, key):
        bucket_index = self._my_hash(key)
        selected_bucket = self.hash_list[bucket_index]
        selected_key = None
        # It will search through the bucket list
        for i in selected_bucket:
            if key == i[0]:
                selected_key = i[1]
                return selected_key
        if selected_key is None:
            return None

    # to get hashtable length
    def hash_length(self):
        return len(self.hash_list)


# todo may delete it
class HashTable:
    # the constructor. It will have the initial capacity of the hash table as parameter
    def __init__(self, capacity):
        # creates an empty buckets list.
        self.hash_list = []
        # creates an empty list for each bucket to handle collisions
        for bucket in range(capacity):
            self.hash_list.append([])

    # to inset a new item into the hash table
    def insert(self, key):
        # the hash function.
        # to determine to which bucket each item will go
        bucket = hash(key) % len(self.hash_list)
        # to get the bucket selected by the hash function
        selected_bucket = self.hash_list[bucket]
        # to insert the item into the bucket
        selected_bucket.append(key)

    # to search for a specific item
    def search(self, key):
        # to get the bucket for the wanted item
        item_bucket = hash(key) % len(self.hash_list)
        selected_bucket = self.hash_list[item_bucket]
        # to search inside the bucket list
        if key in selected_bucket:
            index = selected_bucket.index(key)
            return selected_bucket[index]

        else:
            return None


