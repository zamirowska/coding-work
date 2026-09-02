sen=input('enter a sentences')
vowel=('a','e','i','o','u')
counter =0
for x in sen:
    if x in vowel:
        counter = counter+1
print('the amounr od vowels',counter)        