def num_func(var1,var2):
    side3= ((side1**2+side2**2)**0.5)
    return(side3)
side1=input('enter the lengthof side1:')
side1=float(side1)
side2=input('enter the lengthof side2:')
side2=float(side2)
value=num_func(side1,side2)
print(value)