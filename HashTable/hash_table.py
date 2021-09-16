#
# Linear probing stores the value in the next available position
# Separate chaining uses lists to deal with collisions.
# A linked list is used so that a hash can store multiple values
#
class HashTable:
  class Node:
    def __init__(self, hash, value):
      self.hash = hash
      self.value = value
  
  class Bucket:
    def __init__(self):
      self.nodes = []
  
  def __init__(self):
    self.buckets = [self.Bucket() for _ in range(10)]
  
  def put(self, key, value):
    key = hash(key) % len(self.buckets)
    self.buckets[key].nodes.append(self.Node(hash(key), value))
  
  def get(self, key):
    key = hash(key) % len(self.buckets)
    bucket = self.buckets[key]
    for node in bucket.nodes:
      if node.hash == hash(key):
        return node.value


t = HashTable()
t.put('hello', 'lol')
t.put('hello2', 'lol2')
print(t.get('hello'))