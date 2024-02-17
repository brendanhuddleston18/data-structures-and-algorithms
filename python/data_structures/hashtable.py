from data_structures.linked_list import LinkedList


class Hashtable:
    """
    Hashtable class with set, get, has, key, and hash method
    """

    def __init__(self, size=1024):
        # initialization here
        self.size = size
        self.buckets = [None] * size

    def __hash(self, key):
        index = 0
        prime_number = 599
        for char in key:
            index += ord(char)
        index *= prime_number
        index = index % self.size

    def set(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        # if bucket is None:
        #     bucket = LinkedList()
        #     self.buckets[index] = bucket

        # current_bucket = bucket.head

        # while current_bucket:
        #     pass

        kv_pair = [key, value]
        bucket.insert(kv_pair)

    def get(self, key):
        bucket = self.buckets

        current_bucket = bucket.head

        while current_bucket:
            if current_bucket.value == key:
                return current_bucket.value[1]
            else:
                current_bucket = current_bucket.next
