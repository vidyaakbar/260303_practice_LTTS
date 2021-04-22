# second smallest element

def find_length(list):
    length = len(list)
    list.sort()
    print("second smallest element is ", list[1])


list = [1, 2, 3, 4]
largest = find_length(list)

