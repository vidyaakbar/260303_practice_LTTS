# Merging two Dictionaries

def merge(dict1, dict2):
    return (dict2.update(dict1))

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}


print(merge(dict1, dict2))

print(dict2)

# Convert a list into a nested dictionary of keys

num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)
