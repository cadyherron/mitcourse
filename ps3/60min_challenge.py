def not_string(input_string):
    if input_string[0:3] == 'not ':
        return input_string
    else:
        return "not " + input_string

# print not_string("nothing Hi")


def flim_flam():
    i = 1
    while i <= 100:
        if i % 15 == 0:
            print "FLIMFLAM"
        elif i % 3 == 0:
            print "FLIM"
        elif i % 5 == 0:
            print "FLAM"
        else:
            print i
        i += 1

# print flim_flam()


def no_dupes(array):
    array_to_return = []
    for item in array:
        if item not in array_to_return:
            array_to_return.append(item)
    return array_to_return


# array = [1, 4, 2, 7, 3, 1, 2, 8]
# array2 = [100, 32, 44, 44, 23, 32, 44]
# print no_dupes(array2)
