mood=input('enter your mood ')
weather=input('enter the weather outside')
if mood == 'happy' and weather == 'sunny':
    print('suggesed playlist: Pop hits')
elif mood == 'happy' and weather == 'rainy':
    print('suggesed playlist: Top charts')
elif mood == 'sad' and weather == 'rainy':
    print('suggesed playlist: sad Acoustic')
elif mood == 'sad' and weather == 'windy':
    print('suggesed playlist: top charts')
elif mood == 'relaxed' :
    print('suggesed playlist:Chill Vibes')
else :
    print('default')