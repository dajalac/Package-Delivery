# my custom hash table class
# it has the functionality to add a key and search for a value
# Big O notation O(n)


class MyHashTable:
    # the constructor. It will have the initial capacity of the hash table as parameter
    # big O notation of O(1)
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
        return index

    # to add the key and value into the hash table
    # it has a big O notation of O(1)
    def add(self,key,value):
        bucket_index = self._my_hash(key)
        item_to_add = [key, value]
        # selected_bucket is the bucket selected by the hash function
        selected_bucket = self.hash_list[bucket_index]
        # Since each bucket has a list, it will append the key and value to the bucket list
        selected_bucket.append(item_to_add)


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

    # to remove a item from the hash table
    # Big O notation of O(n)
    def remove (self, key):
        bucket_index = self._my_hash(key)
        selected_bucket = self.hash_list[bucket_index]
        selected_key = None
        # It will search through the bucket list
        for i in selected_bucket:
            if key == i[0]:
                selected_bucket.pop(i[0])

    # to get hashtable length
    # it has a big O notation of O(1)
    def hash_length(self):
        return len(self.hash_list)




