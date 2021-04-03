def sum_square(num_list):
    sum = 0
    for x in num_list:
        print("x is", x)
        if x > 0:
            sum = sum + (x*x)
    return [sum]


print(sum_square([2, -1, 3]))

