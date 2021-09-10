#!/usr/bin/env python

class Queue:
    def __init__(self, size = 10):
        self.__list = [None] * size

    def append(self, elem):
        if self.__list[-1] is not None:
          raise 'Queue is full'
        for i, e in enumerate(self.__list):
          if e is not None:
            self.__list[i] = elem
            return

    def pop(self):
        if len(self.__list) == 0:
            return None
        elem = self.__list[0]
        self.__list.remove(elem)
        return elem

    def as_list(self):
        return list(self.__list)


queue = Queue()

queue.append('Sarah')
queue.append('Susan')
queue.append('Steven')
queue.append('Ian')

print(queue.pop())
print(queue.as_list())
