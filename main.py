from random import randint

def base():
    t = ['Paper', 'Scissors', 'Rock']

    compute =  t[randint(0,2)]

    user_input = input(str('Choose Rock, Paper or Scissors: '))
    user_input = user_input.lower

    if user_input not in t:
        print('Wrong answer')
    elif user_input == compute:
        print('Tie')
    elif user_input == 'Rock':
        if compute == 'Paper':
            print('You lose')
        elif compute == 'Scissors':
            print('You win')
    elif user_input == 'Paper':
        if compute == 'Rock':
            print('You lose')
        elif compute == 'Scissors':
            print('You win')
    elif user_input == 'Paper':
        if compute == 'Rock':
            print('You win')
        elif compute == 'Scissors':
            print('You lose')

base()