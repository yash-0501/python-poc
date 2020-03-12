def topTen():
    yield 5
    yield 6
    yield 7


values = topTen()

print(values)
print(values.__next__())
print(values.__next__())
print(values.__next__())

#generator gives an object