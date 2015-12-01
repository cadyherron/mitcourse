def binary_search(list, element, low, high):
    if high - low < 2:
        return list[low] == element or list[high] == element
    mid = low + int((high - low)/2)
    if list[mid] == element:
        return True
    if list[mid] > element:
        return binary_search(list, element, low, mid - 1)
    else:
        return binary_search(list, element, mid + 1, high)


def selective_sort(list):
    """
    Assume list is a list of element that can be compared using >
    :return: list, sorted in ascending order
    """
    for i in range(len(list) - 1):
        min_index = i
        min_value = list[i]
        j = i + 1
        while j < len(list):
            if min_value > list[j]:
                min_index = j
                min_value = list[j]
            j += 1
        accum = list[i]
        list[i] = list[min_index]
        list[min_index] = accum
    return list

# list = [5, 4, 3, 2, 1]
# print selective_sort(list)


def merge(left, right, lt):
    """
    :param left: sorted list
    :param right: sorted list
    :param lt: defines an ordering of the elements in the lists
    :return: new list, sorted by lt
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if lt(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def sort(list, lt=lambda x, y: x < y):
    """
    :return: new sorted list with the same elements as list
    """
    if len(list) < 2:
        return list[:]
    else:
        middle = int(len(list)/2)
        left = sort(list[:middle], lt)
        right = sort(list[middle:], lt)
        print left, right
        return merge(left, right, lt)


# list = [35, 4, 5, 29, 17, 58, 0]
# newL = sort(list)
# print 'Sorted list =', newL
# list2 = [1.0, 2.25, 24.5, 12.0, 2.0, 23.0, 19.125, 1.0]
# newL = sort(list2, float.__lt__)
# print 'Sorted list =', newL


def last_name_first_name(name1, name2):
    import string
    # first name is everything before space, name1[0]
    name1 = string.split(name1, ' ')
    # last name is everything after the space, name2[1]
    name2 = string.split(name2, ' ')
    if name1[1] != name2[1]:
        return name1[1] < name2[1]
    else:
        return name1[0] < name2[0]


# name1 = "Julia Herron"
# name2 = "Greg Flanagan"
# print last_name_first_name(name1, name2)


def first_name_last_name(name1, name2):
    import string
    name1 = string.split(name1, ' ')
    name2 = string.split(name2, ' ')
    if name1[0] != name2[0]:
        return name1[0] < name2[0]
    else:
        return name1[1] < name2[1]

L = ['John Guttag', 'Tom Brady', 'Chancellor Grimson', 'Gisele Brady']
newL = sort(L, last_name_first_name)
print 'Sorted list =', newL
newL = sort(L, first_name_last_name)
print 'Sorted list =', newL

