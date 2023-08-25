from a1q4 import intro, travel_to_camp, setup_trap, sound_horn, basic_hunt, end

'''
Answer for Question 5 - The Training Again

Name:Minjae Kim
SID:530009478
unikey:mkim9138

'''

'''
We recommend you import your 'q4' module to complete this question.
It will save trouble in needing to copy and paste code from previous question.
However if you wish not to, you are free to remove the import below.
'''

# you can make more functions here if you please
# or any global variables


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
    travel_to_camp()
    # the first element of the returning tuple; selected trap
    # is assigned to trap
    trap = training()
    valid = True
    # while loop breaks when the condition is no longer true.
    while valid is True:
        # if repeat() is no, return the trap that user selected.
        user_input = repeat()
        if user_input == 'no':
            valid = False
        else:
            training()


if __name__ == '__main__':
    main()