class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.order=[]

    def get(self, key: int) -> int:
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key]=value
            self.order.remove(key)
            self.order.append(key)
        else:
            self.order.append(key)
            self.cache[key]=value
            if len(self.order)>self.capacity:
                self.cache.pop(self.order[0])
                self.order.pop(0)
