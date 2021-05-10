import random

print('easy    medium    hard    extreme')
diff = input('Choose a difficulty: ')



if(diff == 'easy'):

    num = random.randint(0, 10)

    print('if you put a answer that isnt a number it will crash :)')
    guess = int(input('Guess a number from 1 to 10: '))
   

    win = 'false'

    chances = 5

    while (chances > 0):

        if(guess == num):
            if(win == 'false'):
                print('you win!')
                win = 'true'

        elif(guess > num):
            print('guess is too high     Chances Left: ' + str(chances))
            guess = int(input('Try again: '))

        elif(guess < num):
            print('guess is too low     Chances Left: ' + str(chances))
            guess = int(input('Try again: '))

        else:
            print('that wasnt a number :)')

        chances -= 1

    if(win == 'false'):
        print('Game Over')

elif(diff == 'medium'):

    num = random.randint(0, 100)

    print('if you put a answer that isnt a number it will crash :)')
    guess = int(input('Guess a number from 1 to 100: '))
   

    win = 'false'

    chances = 7

    while (chances > 0):

        if(guess == num):
            if(win == 'false'):
                print('you win!')
                win = 'true'

        elif(guess > num):
            print('guess is too high     Chances Left: ' + str(chances))
            guess = int(input('Try again: '))

        elif(guess < num):
            print('guess is too low     Chances Left: ' + str(chances))
            guess = int(input('Try again: '))

        else:
            print('that wasnt a number :)')

        chances -= 1

    if(win == 'false'):
        print('Game Over')

elif(diff == 'hard'):

    num = random.randint(0, 200)

    print('if you put a answer that isnt a number it will crash :)')
    guess = int(input('Guess a number from 1 to 200: '))
    

    win = 'false'

    chances = 15

    while (chances > 0):

        if(guess == num):
            if(win == 'false'):
                print('you win!')
                win = 'true'

        elif(guess > num):
            print('guess is too high     Chances Left: ' + str(chances))
            guess = int(input('Try again: '))

        elif(guess < num):
            print('guess is too low     Chances Left: ' + str(chances))
            guess = int(input('Try again: '))

        else:
            print('that wasnt a number :)')

        chances -= 1

    if(win == 'false'):
        print('Game Over')

elif(diff == 'extreme'):

    num = random.randint(0, 1000)

    print('if you put a answer that isnt a number it will crash :)')
    guess = int(input('Guess a number from 1 to 1000: '))
    

    win = 'false'

    chances = 20

    while (chances > 0):

        if(guess == num):
            if(win == 'false'):
                print('you win!')
                win = 'true'

        elif(guess > num):
            print('guess is too high     Chances Left: ' + str(chances))
            guess = int(input('Try again: '))

        elif(guess < num):
            print('guess is too low     Chances Left: ' + str(chances))
            guess = int(input('Try again: '))

        else:
            print('that wasnt a number :)')

        chances -= 1

    if(win == 'false'):
        print('Game Over')



else:
   print('That wasnt an option :)')

   
