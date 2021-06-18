from dataclasses import dataclass

def bubble_sort(items, comparator):
    sorted = False
    while not sorted:
        sorted = True
        for index, curr in enumerate(items):
            if index + 1 == len(items):
                continue
            next = items[index + 1]
            if comparator(curr) > comparator(next):
                items[index + 1] = curr
                items[index] = next
                sorted = False
    return items


@dataclass
class X:
    age: int
    name: str

vars = [
    X(50, 'old'),
    X(30, 'midlife crisis'),
    X(13, 'andy'),
]

def comparator(x): return x.age
def id(x): return x

from random import randint
randoms = [randint(0, 50) for _ in range(0, 20)]
print(bubble_sort(randoms, id))
