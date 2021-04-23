# second smallest element

def find_length(lists):
    length = len(lists)
    lists.sort()
    print("second smallest element is ", lists[1])


lists = [1, 2, 3, 4]
find_length(list)

# change nth value with (n+1)th value


list1 = [0, 1, 2, 3, 4, 5]
n = 2
new_list = []
for i in range (0, len(list1), n):
    new_list.append(list1[i+1])
    new_list.append(list1[i])

print(new_list)


