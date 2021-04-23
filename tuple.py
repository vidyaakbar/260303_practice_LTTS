# repeated items in tuple

tup = (1, 1, 2, 2, 3, 4, 4)

for i in tup:
    if tup.count(i)>1:
        print("duplicate", tup.count(i))


# list to dictionaries

def convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di

tups = [("aaa", 10), ("bbb", 20)]
dictionary = {}
print(convert(tups, dictionary))