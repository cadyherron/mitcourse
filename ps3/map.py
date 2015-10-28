"""
Write a function, map, that takes a list and a function as inputs

map applies the function to each element in the list and
returns a list of each transformed element

list = [1, 2, 3]
function(x) = x + 1
return: [2, 3, 4]
"""


def function(x):
    return x + 1

list = [1, 2, 3]


def map_recursive(list, function):
    if not list:
        return []
    else:
        return [function(list[0])] + map_recursive(list[1:], function)

print map_recursive(list, function)

# def map(function, list):
#     result = []
#     for i in list:
#         result.append(function(i))
#     return result


# def map(function, list):
#     for i in list:
#         yield function(i)



