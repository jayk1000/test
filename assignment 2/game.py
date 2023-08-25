'''
This file should borrow code from your Assignment 1.
However, it will require some modifications for this assignment.

Author:Minjae Kim
SID:530009478
Unikey:mkim9138
'''

'''
Keep this line!
'''
import random

'''
We recommend you import your 'name', 'train' and 'shop' modules to complete this 
question. It will save trouble in needing to copy and paste code from previous 
questions. However if you wish not to, you are free to remove the imports below.
Feel free to import other modules that you have written.
'''
from q1 import introdution
import name
import train
import shop

# you can make more functions or global read-only variables here if you please!


def train_or_not(name_selected):
    '''
    Player can skip the training by inputting print
    after the training or skipping, player have three choice
    1. Exit the game
    2. Join the Hunt
    3. The Cheese shop
    '''
    trap = 'Cardboard and Hook Trap'
    name_selected = input('What\'s ye name, Hunter?\n')
    # if the name is valid, print the selected name.
    if name.is_valid_name(name_selected):
        print(f'Welcome to the Kingdom, Hunter {name_selected}!')
    # if the name is not valid, print name as Bob.
    if not name.is_valid_name(name_selected):
        name_selected = 'Bob'
        print(f'Welcome to the Kingdom, Hunter {name_selected}!')
    print('Before we begin, let\'s train you up!')
    enter_or_skip = 'Press "Enter" to start training or "skip" to Start Game: '
    discontinue = input(enter_or_skip).lower().strip()
    if discontinue != 'skip' and discontinue != chr(27):
        print('')
        # This finds the variable named trap
        # in the main() of train.py and stores the value.
        trap = train.main()
        if type(trap) != str:
            trap = 'Cardboard and Hook Trap'
    else:
        pass
    return trap, name_selected


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
        selection = input('').strip()
        if selection == '1':
            break
        elif selection == '2':
            if is_armed[0]:
                trap_cheese = is_armed[1]
            else:
                trap_cheese = None
            gold, points = hunt(gold, cheese, trap_cheese, points)
        elif selection == '3':
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
            is_armed = change_cheese(name_selected, trap, cheese, e_flag)


def get_game_menu():
    '''
    Returns a string displaying all possible actions at the game menu.
    '''
    menu = '''1. Exit game
2. Join the Hunt
3. The Cheese Shop
4. Change Cheese'''
    return menu


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
                    if ans_cheese == cheese[x][0].lower():
                        if cheese[x][1] == 0:
                            print('Out of cheese!')
                            placeholder = False
                            y = 9
                            print('')
                            continue
                        ans_arm = input(f'Do you want to arm your trap with {cheese[x][0]}? ').lower().strip()
                        if ans_arm == 'back':
                            return (trap_status, trap_cheese)
                        elif ans_arm == 'no':
                            y = 9
                            placeholder = False
                            print('')
                            continue
                        elif ans_arm == 'yes':
                            trap_status = True
                            trap_cheese = cheese[x][0]
                            print(f'{trap} is now armed with {cheese[x][0]}!')
                            return (trap_status, trap_cheese)
                    x += 1
                    if x == len(cheese):
                        print('No such cheese!')
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


def consume_cheese(to_eat: str, cheese: list) -> None:
    '''
    Handles the consumption of cheese.
    Will modify the cheese list, if required.
    Parameters:
        to_eat:    str,        the type of cheese to consume during the hunt.
        cheese:    list,       all the cheeses and quantities the player
                               currently posseses.
    '''
    z = 0
    while z < len(cheese):
        if cheese[z][0] == to_eat:
            break
        z += 1
    cheese[z][1] -= 1


def main():
    '''
    Implement your code here.
    '''
    introdution()
    print('')
    trained = train_or_not(name_selected)
    game_play(trained[0], trained[1])


if __name__ == '__main__':
    name_selected = str
    main()
