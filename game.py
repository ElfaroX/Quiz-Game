import os

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

hello = input('What is your name?\n') 

os.system('cls') # clear the screen and move the cursor to the top-left corner again
print(f'Hello {hello}, please answer the following questions.')


