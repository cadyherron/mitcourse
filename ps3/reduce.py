# def reduce[A,B](list[A], f: (A, B) => B, initial: B): B
# initial: B the the starting value for B

# Reduce takes a list of some type [A] and a function that takes two arguments, A and B. The type A is the type of the
# elements in the list and B the type of the reduced list. An example of a function that might be passed in is
# def intStringAppend(i: Int, s: String): String => s + i.toString


def sum(integer, integer2):
    return integer + integer2


my_list = [1, 2, 3, 4]


def reduce_me(list, function, start):
    """
    :param list: made up of type A
    :param function: takes two arguments, A and B; A is an item of the list, B is the reduced list
    :param start:
    :returns: B, the reduced list
    """
    accum = start
    if not list:
        return accum
    else:
        for i in list:
            accum = function(accum, i)
        return accum

print reduce_me(my_list, sum, 0)


def reduce_recurs(list, function, start):
    def go(my_list, accum):
        if not my_list:
            return accum
        else:
            return go(my_list[1:], function(accum, my_list[0]))
    return go(list, start)

print reduce_recurs(my_list, sum, 10)
