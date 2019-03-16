
def sum_multiple_below_1000():

    sum = 0

    for x in range(0,999):
        if x % 3 == 0 or x % 5 == 0:
            sum = sum + x

    return sum


