'''
Answer for Question 4 - The Training

Name:Minjae Kim
SID:530009478
unikey:mkim9138

'''
no_trap = 'Cardboard and Hook Trap'
cheese = 0


def intro():
    '''
    Prints the introduction by Larry.
    Only line to print:
    "Larry: I'm Larry. I'll be your hunting instructor."
    '''
    print('Larry: I\'m Larry. I\'ll be your hunting instructor.')


def travel_to_camp():
    '''
    Prints the game conversation of travelling and reaching the camp.
    First line to print:
    "Larry: Let's go to the Meadow to begin your training!"
    Last line to print:
    "Larry: This is your camp. Here you'll set up your mouse trap."
    Input from the user should be taken in once in this function.
    '''
    print('Larry: Let\'s go to the Meadow to begin your training!')
    no_camp = input('Press Enter to travel to the Meadow...')
    if no_camp == chr(27):
        return str
    print('Travelling to the Meadow...')
    print('Larry: This is your camp. Here you\'ll set up your mouse trap.')


def setup_trap(enchanted=False) -> tuple:
    '''
    Prints the game conversation of getting your first trap and setting it.
    First line to print:    "Larry: Let's get your first trap..."
    Last line to print:     Either "Larry places one cheddar on the trap!", or
                            "Larry: Odds are slim with no trap!"
                            depending on if you chose a trap or not.
    Input from the user should be taken in twice this function.
    Returns:
        A tuple containing 2 elements:
        1. trap,            str
            - If a trap was chosen, the value is the name of the trap
              e.g. 'High Strain Steel Trap'
            - If no trap was chosen, the value is 'Cardboard and Hook Trap'
              (this will be useful in later questions)
        2. cheddar,         int
            - If a cheese was placed, value is 1
            - If no cheese was placed, value is 0
    '''
    print('Larry: Let\'s get your first trap...')
    user_input = input('Press Enter to view traps that Larry is holding...')
    if user_input == chr(27):
        return None
    left_trap = ('left', 'High Strain Steel Trap', 'One-time Enchanted High Strain Steel Trap')
    right_trap = ('right', 'Hot Tub Trap', 'One-time Enchanted Hot Tub Trap')
    print(f'Larry is holding...\nLeft: {left_trap[1]}\nRight: {right_trap[1]}')
    trap = input('Select a trap by typing "left" or "right": ').lower().strip()
    if trap == chr(27):
        return None
    trap_select = trap.lower().strip()
    if trap_select == left_trap[0]:
        print(f'Larry: Excellent choice.\nYour "{left_trap[1]}" is now set!')
        print('Larry: You need cheese to attract a mouse.')
        print('Larry places one cheddar on the trap!')
        if enchanted:
            return (left_trap[2], 1)
        return (left_trap[1], 1)
    elif trap_select == right_trap[0]:
        print(f'Larry: Excellent choice.\nYour "{right_trap[1]}" is now set!')
        print('Larry: You need cheese to attract a mouse.')
        print('Larry places one cheddar on the trap!')
        if enchanted:
            return (right_trap[2], 1)
        return (right_trap[1], 1)
    else:
        print('Invalid command! No trap selected.')
        print('Larry: Odds are slim with no trap!')
        return (no_trap, cheese)


def sound_horn() -> str:
    '''
    Prints the game conversation to sound horn
    First line to print:    "Sound the horn to call for the mouse..."
    Last line to print:     'Sound the horn by typing "yes": '
    Input from the user should be taken in once this function.
    Returns:
        horn input:     str, the input entered by user for sounding horn
        e.g. 'yes'
        e.g. 'asdhasjkhdsa'
    '''
    print('Sound the horn to call for the mouse...')
    horn = input('Sound the horn by typing "yes": ')
    horn_strip = horn.lower().strip()
    return horn_strip


def basic_hunt(cheddar: int, horn_input: str) -> bool:
    '''
    Prints the hunt and Larry's feedback of hunt.
    The outcome of hunt is determined by the number of cheddar and horn input.
    First line to print:   Varies depending on the hunt.
                        Could be "Caught a Brown Mouse!" or "Nothing happens."
                        or "To catch a mouse, you need both trap and cheese!"
    Last line to print:     Varies depending on the hunt like above.
    Parameters:
        cheddar:        int, the number of cheddar
        horn_input:     str, the input entered by user for sounding horn
    Returns:
        hunt status:    bool, whether the hunt succeeded or not
    '''
    user_horn = horn_input == 'yes'
    # cheddar does not need == 1 as 1 is the same as True.
    if (cheddar and user_horn):
        print('Caught a Brown mouse!')
        print('Congratulations. Ye have completed the training.')
        return True
    elif user_horn == chr(27):
        return None
    else:
        print('Nothing happens.')
        if (cheddar and not user_horn) or (not cheddar and user_horn):
            print('To catch a mouse, you need both trap and cheese!')
        return False


def end(hunt_status: bool):
    '''
    Prints the 'Good luck~' message if hunt was successful
    Parameters:
        hunt_status:    bool, whether the hunt succeeded or not
    '''
    if hunt_status:
        print('Good luck~')
    pass


def main():
    pass


'''
This statement is true if you run this script.
This statement is false if this file is to be imported from another script.
'''
if __name__ == '__main__':
    main()