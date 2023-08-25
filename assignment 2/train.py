'''
Answer for Question 5 - The Training Again from Assignment 1.

Author:Minjae Kim
SID:530009478
unikey:mkim9138
'''

# you can make more functions or global read-only variables here if you please!
from a1q4 import intro, travel_to_camp, setup_trap, sound_horn, basic_hunt, end


def repeat():
    '''
    Returns the user input
    '''
    enter = '\nPress Enter to continue training and "no" to stop training: '
    discontinue = input(enter).lower().strip()
    if discontinue == chr(27):
        return True
    return discontinue


def training():
    '''
    calls the q4 functions
    and returns the first tuple of setup_trap in q4
    which is trap that user selected.
    '''
    correct: tuple = setup_trap()
    if type(correct) != tuple:
        return None
    horning = sound_horn()
    if horning == chr(27):
        return None
    result: bool = basic_hunt(correct[1], horning)
    if type(result) != bool:
        return None
    end(result)
    return correct[0]


def main():
    '''
    Implement your code here.
    '''
    intro()
    if travel_to_camp() == str:
        return None
    # the first element of the returning tuple; selected trap
    # is assigned to trap
    trap = training()
    if type(trap) != str:
        return None
    # while loop breaks when the condition is no longer true.
    a = 1
    while a == 1:
        user_input = repeat()
        # if repeat() is no, return the trap that user selected.
        if user_input == 'no' or type(user_input) == bool:
            a = 0
        else:
            enter = training()
            if type(enter) != str:
                a = 0
    return trap


if __name__ == '__main__':
    main()


