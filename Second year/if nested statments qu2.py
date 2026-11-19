income=input('enter your monthly income')
income=float(income)
age=input('enter your age')
age=int(age)
habit=input('enter your spending habits')
if income <= 2000 :
    if 20< age <40:
        if habit=='high':
            print('app sugests basic saving plan,monthly you need to save 417')
elif income < 5000 :
     if habit=='moderate':
         print('standard saving plan, monthly saving target',income/5)
elif income > 5000 :
    if 30>age:
         if habit=='low':
             print('aggresive Investment plan,projected saving',income/10)*5
else:
    print('Flexible budget plan with general tips to improve savings')