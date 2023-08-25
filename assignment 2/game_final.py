'''
Answer for Question 7 - PIAT: Improved Full Game.

Author: Minjae Kim
SID: 530009478
Unikey: mkim9138
'''
import random
import a1name
from setup import installation, verification
from game import get_game_menu, consume_cheese, change_cheese
from name import is_valid_name, generate_name
import train
import shop

left_trap = ('left', 'High Strain Steel Trap', 'One-time Enchanted High Strain Steel Trap')
right_trap = ('right', 'Hot Tub Trap', 'One-time Enchanted High Strain Steel Trap')

def change_cheese(hunter_name: str, trap: str, cheese: list, e_flag: bool = False) -> tuple:
    '''
    Handles the inputs and ouputs of the change cheese feature.
    Parameters:
        hunter_name: str,        the name of the player.
        trap:        str,        the trap name.
        cheese:      list,       all the cheese and its quantities the player
                                 currently possesses.
        e_flag:      bool,       if the trap is enchanted, this will be True.
                                 default value is False.
    Returns:
        trap_status: bool,       True if armed and False otherwise.
        trap_cheese: str | None, the type of cheese in the trap. if player
                                 exits the function without without arming
                                 trap succesfully, this value is None.
    '''
    trap_status = False
    trap_cheese = None
    while True:
        placeholder = True
        print('')
        print(f'Hunter {hunter_name}, you currently have:')
        z = 0
        while z < len(cheese):
            print(f'{cheese[z][0]} - {cheese[z][1]}')
            z += 1
        y = 10
        print('')
        while y == 10:
            ans_cheese = input('Type cheese name to arm trap: ').lower().strip()
            if ans_cheese == 'back':
                return (trap_status, trap_cheese)
            else:
                x = 0
                while x < len(cheese) and placeholder:
                    if ans_cheese == cheese[x][0].lower().strip():
                        if cheese[x][1] == 0:
                            print('Out of cheese!')
                            placeholder = False
                            y = 9
                            print('')
                            continue
                        ans_arm = input(f'Do you want to arm your trap with {cheese[x][0]}? ').lower().strip()
                        if ans_arm == 'back':
                            return (trap_status, trap_cheese)
                        if ans_arm == 'no':
                            y = 9
                            placeholder = False
                            print('')
                            continue
                        if ans_arm == 'yes':
                            trap_status = True
                            trap_cheese = cheese[x][0]
                            print(f'{trap} is now armed with {cheese[x][0]}!')
                            return (trap_status, trap_cheese)
                    x += 1
                    if x == len(cheese):
                        print('No such cheese!')
                        x = 3
                        y = 9
                        print('')


def hunt(gold: int, cheese: list, trap_cheese: str | None, points: int) -> tuple:
    '''
    Handles the hunt mechanic.
    It includes the inputs and outputs of sounding the horn, the result of
    the hunt, the gold and points earned, and whether users want to continue
    after failing consecutively.
    The function will modify the cheese list, if required.
    Parameters:
        gold:        int,        the quantity of gold the player possesses.
        cheese:      list,       all the cheese and quantities the player
                                 currently posseses.
        trap_cheese: str | None, the type of cheese that the trap is currently
                                 armed with. if its not armed, value is None.
        points:      int,        the quantity of points that the player
                                 currently posseses.
    Returns:
        gold:        int,        the updated quantity of gold after the hunt.
        points:      int,        the updated quantity of points after the hunt.
    '''
    hunt_or_not = ''
    counter = 0
    z = 0
    while z < len(cheese):
        if cheese[z][0] == trap_cheese:
            break
        z += 1
    while True:
        if counter == 5:
            if input("Do you want to continue to hunt? ") == 'no':
                break
            else:
                counter = 0
        hunt_or_not = train.sound_horn()
        if hunt_or_not == 'stop hunt':
            break
        elif hunt_or_not == 'yes':
            if type(trap_cheese) != str:
                print('Nothing happens. You are out of cheese!')
                counter += 1
            elif cheese[z][1] < 1:
                print('Nothing happens. You are out of cheese!')
                counter += 1
            else:
                hunt_success = random.random()
                if hunt_success > 0.5:
                    print('Nothing happens.')
                    counter += 1
                else:
                    print('Caught a Brown mouse!')
                    gold += 125
                    points += 115
                    counter = 0
                consume_cheese(trap_cheese, cheese)
        else:
            print('Do nothing.')
            counter += 1
        # print is shown at the end of each hunt.
        print(f'My gold: {gold}, My points: {points}\n')
    return (gold, points)


def game_play(trap, name_selected):
    is_armed = (False, )
    e_flag = False
    choice = str
    gold = 125
    cheese = (["Cheddar", 0], ["Marble", 0], ["Swiss", 0])
    CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))
    points = 0
    while True:
        print(f'\nWhat do ye want to do now, Hunter {name_selected}?')
        print(get_game_menu())
        selection = input('Enter a number between 1 and 4: ').strip()
        if not selection.isdigit():
            print('Invalid input. Try again!')
            continue
        elif int(selection) < 1 or int(selection) > 4:
            print('Must be between 1 and 4.')
            continue
        elif selection == '1':
            break
        elif selection == '2':
            if is_armed[0]:
                trap_cheese = is_armed[1]
            else:
                trap_cheese = None
            gold, points = hunt(gold, cheese, trap_cheese, points)
        elif selection == '3':
            print('')
            print('Welcome to The Cheese Shop!')
            i = 0
            while i < len(CHEESE_MENU):
                print(f'{CHEESE_MENU[i][0]} - {CHEESE_MENU[i][1]} gold')
                i += 1
            choice = 0
            while choice != '3':
                help_ye = ('\nHow can I help ye?\n1. Buy cheese'
                           '\n2. View inventory\n3. Leave shop\n')
                choice = (input(help_ye).strip())
                if not choice.isdigit() or int(choice) < 1 or int(choice) > 3:
                    print('I did not understand.')
                if choice == '2':
                    shop.display_inventory(gold, cheese, trap)
                if choice == '1':
                    gold_spent, cheese_bought = shop.buy_cheese(gold)
                    gold -= gold_spent
                    t = 0
                    while t < len(cheese_bought):
                        cheese[t][1] += cheese_bought[t]
                        t += 1
        elif selection == '4':
            if trap == left_trap[2] or trap == right_trap[2]:
                e_flag = True
            is_armed = change_cheese(name_selected, trap, cheese, e_flag)


def introdution():
    '''
    Prints the title, logo and credits
    '''
    author = 'An INFO1110/COMP9001 Student'
    title = 'Mousehunt'
    logo_line1 = '____()()'
    logo_line2 = '/      @@'
    logo_line3 = '`~~~~~\\_;m__m._>o'
    x = ' '
    logo = (f'\n{x*7}{logo_line1}\n{x*6}{logo_line2}\n{logo_line3}')
    credits = f'''
Inspired by Mousehunt© Hitgrab
Programmer - {author}
Mice art - Joan Stark and Hayley Jane Wakenshaw'''
    print(title)
    print(logo)
    print(credits)


def updated_train(enchanted=False):
    trap = 'Cardboard and Hook Trap'
    print('Before we begin, let\'s train you up!')
    enter_or_skip = 'Press "Enter" to start training or "skip" to Start Game: '
    discontinue = input(enter_or_skip).lower().strip()
    if discontinue != 'skip' and discontinue != chr(27):
        print('')
        # This finds the variable named trap
        # in the main() of train.py and stores the value.
        trap = train.main(enchanted)
        if type(trap) != str:
            trap = 'Cardboard and Hook Trap'
    else:
        pass
    return trap


def run_setup():
    validity = verification('/home/game_master/', '12 May 2023 03:33:40')
    i = 0
    status = False
    while i < len(validity) and not status:
        if validity[i].strip('.') == 'Abnormalities detected':
            status = True
        i += 1
    return status


def personalization(tamper_flag):
    name_selected = str
    if tamper_flag:
        name_selected = input('What\'s ye name, Hunter?\n')
        if a1name.is_valid_name(name_selected):
            print(f'Welcome to the Kingdom, Hunter {name_selected}!')
        else:
            name_selected = 'Bob'
            print(f'Welcome to the Kingdom, Hunter {name_selected}!')
    else:
        name_selected = input('What\'s ye name, Hunter? ')
        if is_valid_name(name_selected):
            print(f'Welcome to the Kingdom, Hunter {name_selected}!')
        else:
            print("That's not nice!")
            print("I'll give ye 3 attempts to get it right or I'll name ye!")
            count = 0
            while count < 3:
                name_selected = input('What\'s ye name, Hunter? ')
                if not is_valid_name(name_selected):
                    count += 1
                    print(f'Nice try. Strike{count}!')
                else:
                    break
            if count == 3:
                print('I told ye to be nice!')
                generate_name(name_selected)
            print(f'Welcome to the Kingdom, Hunter {name_selected}!')
    return name_selected


def main():
    status = run_setup()
    if status:
        repair_opt = input('Do you want to repair the game? ').lower().strip()
        if repair_opt == 'yes':
            installation('/home/game_master/', '12 May 2023 03:33:40')
            status = run_setup() # False
        else:
            print('Game may malfunction and personalization will be locked.')
            ensure = input('Are you sure you want to proceed?').lower().strip()
            if ensure == 'yes':
                print('You have been warned!!!')
            else:
                return
    print('Launching game...')
    print('.')
    print('.')
    print('.')
    introdution()
    print('')
    name = personalization(status)
    trained = updated_train(enchanted=True)
    game_play(trained, name)
    # he will only gift players this enchantment once regardless of the number of times players complete the training. The one-time enchantment gifted by Larry isconsumed when users hunt. 
    # Applicable to the first Hunt immediately after training, this includes if they exit the hunt immediately. Trap is armed with Swiss cheese:  +0.25 attraction rate to Tiny mouse Trap is armed with Marble cheese: +25 gold dropped by Brown mouse only
    # Trap is armed with Cheddar cheese: +25 points dropped by Brown mouse only
    # not to default
    # They must hunt for it to wear off.


if __name__ == '__main__':
    main()