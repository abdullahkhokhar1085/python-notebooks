class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

print(queue.is_empty())





