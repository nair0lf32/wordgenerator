# -*- coding: UTF-8 -*-

import itertools
from termcolor import colored
import time

print(colored('''
#########################################################################################################

Made By:   florian E. (nairolf32)          
     
 _     _ _______ ______   ______  _______ _______ __    _ _______ ______   _______ _______ _______ ______   
| | _ | |       |    _ | |      ||       |       |  |  | |       |    _ | |   _   |       |       |    _ |  
| || || |   _   |   | || |  _    |    ___|    ___|   |_| |    ___|   | || |  |_|  |_     _|   _   |   | ||  
|       |  | |  |   |_||_| | |   |   | __|   |___|       |   |___|   |_||_|       | |   | |  | |  |   |_||_ 
|       |  |_|  |    __  | |_|   |   ||  |    ___|  _    |    ___|    __  |       | |   | |  |_|  |    __  |
|   _   |       |   |  | |       |   |_| |   |___| | |   |   |___|   |  | |   _   | |   | |       |   |  | |
|__| |__|_______|___|  |_|______||_______|_______|_|  |__|_______|___|  |_|__| |__| |___| |_______|___|  |_|

A simple wordlist generator (yes, another one)
Made in python using itertools for random generation. 

##########################################################################################################
        ''', 'green'))

help_msg = '''
Enter A letter corresponding to your choice in the menu prompt
Type the corresponding letter only to choose an operation mode:
- H: is for help and will display this message
- Q: Is to stop and exit the program
- R: Random generation outputs a randomly generated wordlist based upon some choices.
     you can use alpha or alphanumerical mixed with common special characters.
     But be careful with this mode, because of the usage of itertools, the more complex the operation is
     the longer time and memory it will use.
- C: Custom mode. Generate a targeted wordlist with your own given information. 

Note: generated files are re-generated after each run in output folder! grab your files before running again
'''
# random data
alpha_lower = "abcdefghijklmopqrstuvwxyz"
alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeric = "0123456789"
special = " `èéà@ç-/\\:#{}[]()'&*`^$!."

# main loop menu
def menu():
    print("Welcome to my custom wordlist generator! \n")

    while True:
        time.sleep(1)
        print(colored("\nWhat do you need? please Enter the letter corresponding to your choice: \n\n"
                      "Random list (R) - custom list (C) - Help (H)- Quit (Q) \n", 'green'))

        operation_choice = str(input(colored("choice: ", 'magenta')).strip().capitalize())

        # exit
        if operation_choice == 'Q':
            time.sleep(1)
            print(colored("\nGoodbye !", 'red'))
            break
        # help menu
        elif operation_choice == 'H':
            print(colored(help_msg, 'blue'))

        # Random mode menu
        elif operation_choice == 'R':
            print(colored("\nPlease use this mode with caution. The length range should be limited to a maximum of 16."
                          "\nEven this value will take a very long time and make a very big wordlist! use custom mode,"
                          "\nfor a better control, thus a lighter and more precise generation", 'red'))

            print(colored("\nEnter a minimal length", 'green'))
            try:
                min_length = int(input(colored("\nmin_length (1-16) : ", 'magenta')))
            except ValueError:
                print(colored("Invalid input!", 'red'))
            print(colored("\nEnter a maximal length", 'green'))
            try:
                max_length = int(input(colored("\nmax_length (1-16) : ", 'magenta')))
            except ValueError:
                print(colored("Invalid input!", 'red'))

            combinations = []

            print(colored("\ndefault base set is empty. Do you want to add alphabet characters? (Y/N)", 'green'))
            choice = str(input(colored("\nchoice : ", 'magenta')).strip().capitalize())
            if choice == 'Y':
                combinations[:] += alpha_lower
            else:
                pass

            print(colored("\nDo you want to add uppercase characters? (Y/N)", 'green'))
            choice = str(input(colored("\nchoice : ", 'magenta')).strip().capitalize())
            if choice == 'Y':
                combinations[:] += alpha_upper
            else:
                pass

            print(colored("\nAdd numbers? (Y/N)", 'green'))
            choice = str(input(colored("\nchoice : ", 'magenta')).strip().capitalize())
            if choice == 'Y':
                combinations[:] += numeric
            else:
                pass

            print(colored("\nWhat about special characters? (Y/N)", 'green'))
            choice = str(input(colored("\nchoice : ", 'magenta')).strip().capitalize())
            if choice == 'Y':
                combinations[:] += special
            else:
                pass

            generate_random(min_length, max_length, combinations)

        # custom mode menu
        elif operation_choice == 'C':
            print(colored("\nThis mode is targeted and generate a wordlist based on your given words or numbers."
                          "\nAlso this mode can take a very long time and make a very big file, But is more concise!"
                          "\nYou can prepare your data accordingly to your expected results", 'red'))
            combinations = []

            print(colored("\nThis mode takes a single input but it can be many words or numbers", 'green'))
            print(colored("\nInstead of asking them one by one, it takes all you information at once", 'green'))
            print(colored("\nSeparate each data with a comma", 'red'))
            print(colored("\nIt can be usernames, birthdate , ages, phone numbers...", 'green'))
            print(colored("\nyou can even enter single characters, but use COMMA for separation!", 'green'))
            print(colored("\nexample: john,doe,1990,23,bonnie123,1,@,#,bonnie", 'green'))
            print(colored("\nEnter your data below", 'green'))

            data = str(input(colored("\ndata : ", 'magenta')))
            combinations = data.split(sep=',')

            generate_custom(combinations)

        else:
            print("Invalid choice! please try again!")


# random mode generator with itertools.product
def generate_random(min_length, max_length, combinations):
    start_time = time.time()

    with open("./output/random_wordlist.txt", 'r+') as file:
        file.truncate(0)

    for length in range(min_length, max_length + 1):
        for item in itertools.product(combinations, repeat=length):
            word = "".join(item)
            print(word)
            with open("./output/random_wordlist.txt", 'a') as file:
                file.write(word + '\n')

            with open("./output/random_wordlist.txt", 'r') as file:
                for count, line in enumerate(file):
                    pass
            words_number = count + 1

    stats = "\n{0} words generated in {1} seconds".format(words_number, (round((time.time() - start_time), 2)))
    print(colored(stats, 'red'))
    print(colored("\nYour generated wordlist file can be found in the output folder", 'red'))
    time.sleep(1)


# Custom mode generator with itertools.permutations
def generate_custom(combinations):
    start_time = time.time()

    with open("./output/custom_wordlist.txt", 'r+') as file:
        file.truncate(0)
    for length in range(len(combinations)+1):
        for item in itertools.permutations(combinations, length):
            word = "".join(item)
            print(word)
            with open("./output/custom_wordlist.txt", 'a') as file:
                file.write(word + '\n')

            with open("./output/custom_wordlist.txt", 'r') as file:
                for count, line in enumerate(file):
                    pass
            words_number = count + 1

    stats = "\n{0} words generated in {1} seconds".format(words_number, (round((time.time() - start_time), 2)))
    print(colored(stats, 'red'))
    print(colored("\nYour generated wordlist file can be found in the output folder", 'red'))
    time.sleep(1)


if __name__ == "__main__":
    menu()
