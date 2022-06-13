import random

instruction = '''
Welcome to The Rock, Papper, Scisoors Game
      Here,
        1. Rock beats Scissors
        2. Scissors beats Paper
        3. Paper beats Rock
        4. Its a tie when both are same(No winner and the game restarts)
NB: You are required to enter digits only as specified
'''
print(instruction)


def goodbye_message():
    print('Nice Playing with you ❣️')


def play():
    while True:    
        # Array of options to choose 
        choices = ['R','S','P']
        computer_choice = random.choice(choices)
        if computer_choice == 'R':
            computer_text = "Rock"
        elif computer_choice == 'S':
            computer_text = "Scissors"
        elif computer_choice == 'P':
            computer_text = "Paper"

        user_input = input("\nChoose from any of these R or S or P: \n").upper()

        if user_input == 'R':
            user_input_text = "Rock"
        elif user_input == 'S':
            user_input_text = "Scissors"
        elif user_input == 'P':
            user_input_text = "Paper"

            
        if(user_input == 'R' and computer_choice == 'R') or (user_input == 'S' and computer_choice == 'S') or (user_input == 'P' and computer_choice == 'P') :
            print('\'Player '+ "(" + user_input_text +")" + ' : ' + 'CPU (' +  (computer_text) + ")'")
            print('It is a Tie 🤝')
            print('Let\'s play again')

        elif (user_input == 'R' and computer_choice == 'S'):
            print('\'Player '+ "(" + user_input_text +")" + ' : ' + 'CPU (' +  (computer_text) + ")'")
            print('Player Wins 💪')
            goodbye_message()
            break
        elif (user_input == 'S' and computer_choice == 'R'):
            print('\'Player '+ "(" + user_input_text +")" + ' : ' + 'CPU (' +  (computer_text) + ")'")
            print('Computer Wins 💪')
            goodbye_message()
            break

        elif (user_input == 'S' and computer_choice == 'P'):
            print('\'Player '+ "(" + user_input_text +")" + ' : ' + 'CPU (' +  (computer_text) + ")'")
            print('Player Wins 💪')
            break
        elif (user_input == 'P' and computer_choice == 'S'):
            print('\'Player '+ "(" + user_input_text +")" + ' : ' + 'CPU (' +  (computer_text) + ")'")
            print('Computer Wins 💪')
            goodbye_message()
            break

        elif (user_input == 'P' and computer_choice == 'R'):
            print('\'Player '+ "(" + user_input_text +")" + ' : ' + 'CPU (' +  (computer_text) + ")'")
            print('Player Wins 💪')
            goodbye_message()
            break
        elif (user_input == 'R' and computer_choice == 'P'):
            print('\'Player '+ "(" + user_input_text +")" + ' : ' + 'CPU (' +  (computer_text) + ")'")
            print('Computer Wins 💪')
            goodbye_message()
            break

        else:
            print('Invalid input!!!')



# run the code
while True:
    user_decision = input("Are you ready to play? Y or N: ").lower()
    if(user_decision == 'y'):
        play()
        break
    elif user_decision == 'n':
        print('GoodBye!')
        break
    else:
        print("Choose Yes or No")