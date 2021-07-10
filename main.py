import random

person_wins = 0
computer_wins = 0

print('Welcome to Rock, Paper, Scissors!!')


while True:
    user_input = input("\nType r for rock, p for paper, s for scissors, q for quit: ").lower()
    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2
    
    #User wins scenarios
    if(user_input == 'r' and random_number == 2):
        print('You win, the computer chose scissors.')
        person_wins += 1
    
    elif(user_input == 'p' and random_number == 0):
        print('You win, the computer chose rock.')
        person_wins += 1
    
    elif(user_input == 's' and random_number == 1):
        print('You win, the computer chose paper.')
        person_wins += 1

    #Draw scenarios
    elif(user_input == 'r' and random_number == 0):
        print('Draw.')
    
    elif(user_input == 'p' and random_number == 1):
        print('Draw.')
    
    elif(user_input == 's' and random_number == 2):
        print('Draw.')

    #Computer wins scenarios
    elif(user_input == 'r' and random_number == 1):
        print('The computer wins, it chose paper.')
        computer_wins += 1
    
    elif(user_input == 'p' and random_number == 2):
        print('The computer wins, it chose scissors.')
        computer_wins += 1
    
    
    elif(user_input == 's' and random_number == 0):
        print('The computer wins, it chose rock.')
        computer_wins += 1

    elif(user_input == 'q'): 
        print('Your points:', person_wins)
        print('Computer points:', computer_wins)
        break
    
    else:
        pass


     