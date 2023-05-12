import os
import time 

Questions = ["what's 7 + 9",
             "what's 8 * 7",
             "what's ( 9 - 3 ) / 2",
             "what's ( 2 * 3 ) + 2",
             "what's 12 * 11"]

os.system('cls') # clear the screen and move the cursor to the top-left corner
term_width = os.get_terminal_size().columns # get the width of the terminal window
welcome_msg = 'Welcome to my Quiz game!' # calculate the number of spaces needed to center the message
padding = (term_width - len(welcome_msg)) // 2
print(' ' * padding + welcome_msg) # print the message with padding on both sides

play = input('Do you want to play? (yes/no): ')
if play != 'yes':
    quit()

os.system('cls')
user_name = input('What is your name?\n') 

os.system('cls') # clear the screen and move the cursor to the top-left corner again
print(f'Hello {user_name}, please answer the following questions.')

time.sleep(1)

print(Questions[0])

def test(answer):
    if answer == 16:
        print('Your answer is correct')
    else:
        print('Try again')

answer_str = input('Your answer: ')
answer = int(answer_str)  # convert the string to an integer
test(answer)

