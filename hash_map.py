import pprint


class hash_m:

    def __init__(self, elem):
        self.bucket_size = len(elem)
        self.buckets = [[] for i in range(self.bucket_size)]
        self.sey_buckets(elem)

    def sey_buckets(self, elem):
        for key, value in elem:
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size
            self.buckets[index].append((key, value))

    def give_value(self, key):
        hashed_value = hash(key)
        index = hashed_value % self.bucket_size
        bucket = self.buckets[index]
        for _, value in bucket:
            if _ == key:
                return (value)
        return None

    def __str__(self):
        return pprint.pformat(self.buckets)