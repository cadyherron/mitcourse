x = 10.0
for i in range(10):
    x += 0.1
print x == 11.0
for i in range(10):
    x -= 0.1
print x == 10.0


# this will print:
# False
# True


def buildCodeBook():
    letters = '.abcdefghijklnopqrstuvwxyz'
    # empty dict
    codeBook = {}
    key = 0
    for c in letters:
        # make each letter a key in dict
        codeBook[key] = c
        key += 1
    return codeBook


def decode(cypherText, codeBook):
    # empty string
    plainText = ''
    for e in cypherText:
        # if element from cypherText is in codeBook:
        if e in codeBook:
            # add element to empty string
            plainText += codeBook[e]
        else:
            # add space to plainText
            plainText += ' '
    return plainText


codeBook = buildCodeBook()
msg = (3, 2, 41, 1, 0)
print decode(msg, codeBook)

# this will print:
# cb a.
# big Oh complexity of decode == O(n^2)


def add_vectors(v1, v2):
    """
    :param v1: list of ints
    :param v2: list of ints
    :return: list containing pointwise sum of elements in v2 and v2
    add_vectors([4, 5], [1, 2, 3]) returns [5, 7, 3]
    add_vectors([[], []) returns []
    *** does not modify input ***
    """
    vectors = []
    i = 0
    if len(v1) < len(v2):
        while i < len(v1):
            vectors.append(v1[i] + v2[i])
            i += 1
        vectors += v2[i:]
    else:
        while i < len(v2):
            vectors.append(v1[i] + v2[i])
            i += 1
        vectors += v1[i:]
    return vectors


v1 = [12, 3, 1, 4]
v2 = [0, 1, -1]
print add_vectors(v1, v2)
