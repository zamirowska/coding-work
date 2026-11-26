def text_func(var1,var2):
    cat=''
    for letter in var1:
        if letter != var2:
            cat=cat+letter
    return(cat)
word=input('enter a word')
letter = input('enter a letter you want to remove')
value=text_func(word,letter)
print(value)