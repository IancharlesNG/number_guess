# one line comment 

'''
- Multi- line comment 

print(f'It\'s age is {age}')

print(f"It's age is {age}")

print("It's age is " + str(age))
'''

# NUMBER GUESSING GAME
'''
prompts 3 
all 3 correct  -> 10 points
2 correct - > 5
1 correct -> 0
0 correct -> GAME OVER
'''

"""
Levels
Time
"""
import random
scores = 0,

game_numbers = [1,2,3,4,5,6,7,8,9,10]

correct_guesses = 0
game_rounds = 0
all_choices = []

while game_rounds < 3:
    choice_ = random.choice(game_numbers)
    all_choices.append(choice_)
    print("Range 0 - 10")
    guess = int(input("Guess the number: "))
    if choice_ == guess:
        correct_guesses += 1

    if game_rounds == 2:
        if correct_guesses ==0:
            print("Wachana nayo. Hauwezi")
            print(f'correct guesses: {correct_guesses}')
            print(f"These were the numbers: {all_choices} ")

        elif correct_guesses == 1:
            print(f'GOT 1 CORRECT!')
            print(f'correct guesses: {correct_guesses}')
            print(f'YOU SOCRE IS: {0}')
            print(f"These were the numbers: {all_choices} ")
            
        elif correct_guesses == 2:
            print(f'ALL MOST! GOT 2 CORRECT!')
            print(f'correct guesses: {correct_guesses}')
            print(f'YOU SOCRE IS: {5}')
            print(f"These were the numbers: {all_choices} ")

        elif correct_guesses == 3:
            print(f'AWESOME! GOT ALL CORRECT!')
            print(f'YOU SOCRE IS: {10}')
            print(f"These were the numbers: {all_choices} ")

    game_rounds += 1















