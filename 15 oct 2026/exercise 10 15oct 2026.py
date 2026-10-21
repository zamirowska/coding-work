people=input('how many people are you inviting')
people=int(people)
if people < 10 :
    for x in range (people):
        name=input('enter their name')
        print(name,'has been invited')
else:
    print('you invited too much people')