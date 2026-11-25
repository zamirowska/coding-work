def some_function(var1,var2):
    add= var1+var2
    return add
num1=input('enter a number')
num1=float(num1)
num2=input('enter another number')
num2= float(num2)
value = some_function(num1,num2)
print(value)