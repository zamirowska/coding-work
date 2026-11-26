def num_test(var1):
    if num >10:
        return('greater than 10')
    elif num ==10:
        return('equal to 10')
    else :
        return('less than 10')
num=input('enter a number')
num=float(num)
value= num_test(num)
print(value)