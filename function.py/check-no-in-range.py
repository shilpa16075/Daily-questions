# write a python function to check whether the number falls in the given range.
def number_test(n):
    if n in range(6,16):
        print(f'The number {n} falls in the given range')
    else:
        print('Number not found!!!')
number_test(7)