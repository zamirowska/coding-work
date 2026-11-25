def some_function(var1):
    total=0
    for x in var1:
        total=total+1
    return total
word = input('enter a word')
letter=some_function(word)
print(letter)