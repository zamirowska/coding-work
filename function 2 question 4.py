def num_func(var1,var2):
    count=0
    for x in range (var1,var2):
        if x%2 == 0:
            count = count+1
    return count
num=input('enter a number')
num=int(num)
num1=input('enter another number')
num1=int(num1)
value=num_func(num,num1)
print(value)