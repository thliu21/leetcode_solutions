"""
双链表+hash table
"""

class Node:
    def __init__(self, key = -1, value = -1):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def print(self):
        cur = self.head.next
        print("$", end=" ")
        while cur != self.tail:
            print(cur.key, end=" ")
            cur = cur.next
        print("#")

    def print_rev(self):
        cur = self.tail.prev
        print("#", end=" ")
        while cur != self.head:
            print(cur.key, end=" ")
            cur = cur.prev
        print("$")

    def remove_node(self, node):
        left = node.prev
        right = node.next
        node.prev = node.next = None
        left.next = right
        right.prev = left

    def add_tail(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node
    
    def pop_head(self):
        popped_key = self.head.next.key
        self.cache.pop(popped_key)
        second = self.head.next.next
        second.prev = self.head
        self.head.next = second

    def get(self, key: int) -> int:
        ret = -1
        if key in self.cache:
            node = self.cache[key]
            ret = node.value
            self.remove_node(node)
            self.cache[key] = Node(key=key, value=ret)
            self.add_tail(self.cache[key])
        return ret

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.get(key)
        else:
            if self.capacity == 0:
                self.pop_head()
                self.capacity = 1
            new_node = Node(key=key, value=value)
            self.cache[key] = new_node
            self.add_tail(new_node)
            self.capacity -= 1

lRUCache = LRUCache(2)
lRUCache.put(2, 1)
lRUCache.put(2, 2)
print(lRUCache.get(2))
lRUCache.put(1, 1)
lRUCache.put(4, 1)
print(lRUCache.get(2))