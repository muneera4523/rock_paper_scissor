import random
ch=['rock','paper','scissor']
comp=random.choice(ch)
player =''
while player not in ch:
    player=input('enter your choice : rock/paper/scissor:-').lower()

print(f'computer chose {comp} player chose {player}')
if player ==comp:
    print('its a tie!!!!!!!!!!!!!!!')
elif player =='rock':
    if comp =='paper':
        print(f'paper covers rock,computer wins')
    else:
        print('print rock beats scissor player wins')
elif player =='paper':
    if comp =='scissor':
        print('computer wins scissor cut paper')
    else:
        print('paper covers rock player wins')

elif player =='scissor':
    if comp =='rock':
        print('rock beats scissor comp wins')
    else:
        print('scissor cuts paper player wins')


