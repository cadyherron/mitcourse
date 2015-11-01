"""
Write a function, map, that takes a list and a function as inputs

map applies the function to each element in the list and
returns a list of each transformed element

list = [1, 2, 3]
function(x) = x + 1
return: [2, 3, 4]
"""


# global function and list
def function(x):
    return x + 1

list = [1, 2, 3]


def map_simple(function, list):
    result = []
    for i in list:
        result.append(function(i))
    return result


def map_python(function, list):
    for i in list:
        yield function(i)


def map_recursive(list, function):
    if not list:
        return []
    else:
        return [function(list[0])] + map_recursive(list[1:], function)

print map_recursive(list, function)


def julia_tail_map(list, function):
    def go(list, accum):
        if not list:
            return accum
        else:
            return go(list[1:], accum + [function(list[0])])
    return go(list, [])

print julia_tail_map(list, function)



