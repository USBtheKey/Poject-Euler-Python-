list_fibo = []

def fibo_calc():

    first_num = 0
    second_num = 1

    index = 0

    while True:

        fibo_num = first_num + second_num

        if fibo_num > 4000000:
            break

        elif fibo_num % 2 == 0:
            list_fibo.append(fibo_num)
            print(index, ": ", fibo_num)
            index += 1

        first_num = second_num
        second_num = fibo_num

    return sum(list_fibo)









