def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)


# print power(2, 2)
# print power(3, 4)

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

# print factorial(5)


def uniques(array):
    unique_array = []
    for i in array:
        if i not in unique_array:
            unique_array.append(i)
    return unique_array

array = [1, 5, 'frog', 2, 1, 3, 'frog']

# print uniques(array)


def combinations(array1, array2):
    new_combos = []
    for item1 in array1:
        for item2 in array2:
            new_combos.append(item1 + item2)
    return new_combos

array1 = ["on", "in"]
array2 = ["to", "rope"]
# print combinations(array1, array2)


def primes(number):
    if number % 2 != 0:
        return True
    else:
        return False

# print primes(200)


def rectangle_overlap(rect1, rect2):
    """
    :return: True if rectangles overlap (non-inclusive)
    """
    # let's handle bottom-left of rectangle 2 first
    # if bottom-left2 in range(bottom-left1, bottom-right1):
    # then we also care about if our point is within the height bounds
    if rect2[0][0] in range(rect1[0][0] + 1, rect1[1][0]) and rect2[0][1] in range(rect1[0][1] + 1, rect1[1][1]):
        return True
    # now we do top-right corner
    # if top-right2 in range(bottom-left1, bottom-right1):
    # then we also care about if our point is within the width bounds
    elif rect2[1][1] in range(rect1[0][1] + 1, rect1[1][1]) and rect2[1][0] in range(rect1[0][0] + 1, rect1[1][0]):
        return True
    else:
        return False

# rect1 = [[0, 0], [3, 3]]
# rect2 = [[1, 1], [4, 5]]

# rect1 = [[0, 0], [1, 4]]
# rect2 = [[1, 1], [3, 2]]

# rect1 = [[1, 1], [4, 5]]
# rect2 = [[0, 0], [3, 3]]
#
# print rectangle_overlap(rect1, rect2)


def switch_direction(dir):
    if dir == 'right':
        dir = 'left'
    elif dir == 'left':
        dir = 'right'
    return dir

# print switch_direction('right')


def the_counting_game(number_of_players=10, total=100):
    """
    whenever total is divisible by 7, switch directions
    (add later) whenever total is divisible by 11, skip one person
    :return: the number of the player that will say the "total" number, e.g. Player 1
    """
    # a  b  c  d  e  f  g  h  i  j
    # 1  2  3  4  5  6  7
    # 13 12 11 10 9  8
    #                            14
    # 15 16 17 18 19 20 21
    # 27 26 25 24 23 22
    #                            28
    # 29
    # print "total", total
    player_number = 1  # first player will say the number 1
    dir = 'right'  # we start off counting to the right
    num_said = 1  # the number said by the first player
    while num_said < total:
        if dir == 'right':
            print dir
            # if we're at the last player, go back to the first player
            # which is last player minus total number of players minus 1
            if player_number == number_of_players:
                player_number = number_of_players - 1
                print "p", player_number, "said: ", num_said
            else:
                print "p", player_number, "said: ", num_said
                player_number += 1
            # if the next number will be a multiple of 7, time to switch directions
            if (num_said + 1) % 7 == 0:
                print "this should switch", dir
                dir = switch_direction(dir)
                print "this should switch", dir
        elif dir == 'left':
            print dir
            # if this is the first player, going left means going to the last player
            # which is total number of players
            if player_number == 1:
                player_number += (number_of_players - 1)
            else:
                print "p", player_number, "said: ", num_said
                player_number -= 1
            # if the next number will be a multiple of 7, time to switch directions
            if (num_said + 1) % 7 == 0:
                print "this should switch", dir
                dir = switch_direction(dir)
                print "this should switch", dir
        num_said += 1
    return "Player to say the total: " + str(player_number)

print the_counting_game(10, 24)




