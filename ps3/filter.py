"""
filter

input: list
input: function that returns a boolean
    if True keep element in list
    if False remove element
returns: a new list with only the elements that meet a certain condition
"""

list = [5, 6, 7]


def function(x):
    if x == 6:
        return True
    else:
        return False


def filter_function(list, function):
    def go(list, accum):
        if not list:
            return accum
        else:
            # function returns a boolean
            # if you get True, append to your list
            if function(list[0]):
                return go(list[1:], accum + [list[0]])
            else:
                return go(list[1:], accum)
    return go(list, [])

print filter_function(list, function)