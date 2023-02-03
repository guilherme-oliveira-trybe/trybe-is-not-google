from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()
        self.length = 0

    def __len__(self):
        return self.length

    def enqueue(self, value):
        self.queue.append(value)
        self.length += 1

    def dequeue(self):
        if len(self.queue) > 0:
            self.length -= 1
            return self.queue.pop(0)

    def search(self, index):
        if 0 <= index <= len(self.queue):
            return self.queue[index]
        else:
            raise IndexError
