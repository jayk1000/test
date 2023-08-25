'''
Write your solution to 1. Upgraded Cheese Shop here.
It should borrow code from Assignment 1.

Author:Minjae Kim
SID:530009478
Unikey:mkim9138
'''

CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))

# you can make more functions or global read-only variables here if you please!


def buy_cheese(gold: int) -> tuple:
    '''
    Feature for players to buy cheese from shop.
    Parameters:
        gold:           int,    amount of gold that player has
    Returns:
        gold_spent:     int,    amount of gold spent
        cheese_bought:  tuple,  amount of each type of cheese bought
    '''
    cheese_bought = [0, 0, 0]
    gold_spent = 0
    gold_spent_now = 0
    while True:
        print(f'You have {gold} gold to spend.')
        cheese_amount = input('State [cheese quantity]: ').lower().split()
        if not cheese_amount:
            continue
        if len(cheese_amount) == 2:
            x = 0
            while x < len(CHEESE_MENU):
                if cheese_amount[0] == CHEESE_MENU[x][0].lower():
                    if cheese_amount[1].isdigit():
                        cheese_buy = int(cheese_amount[1])
                        gold_spent_now = cheese_buy * CHEESE_MENU[x][1]
                        if cheese_buy > 0 and gold - gold_spent_now >= 0:
                            print(f'Successfully purchase {cheese_buy} {CHEESE_MENU[x][0].lower()}.')
                            cheese_bought[x] += cheese_buy
                            gold_spent += gold_spent_now
                            gold -= gold_spent_now
                        elif cheese_buy <= 0:
                            print('Must purchase positive amount of cheese.')
                        elif gold - gold_spent_now < 0:
                            print('Insufficient gold.')
                        x += 1
                        continue
                    elif cheese_amount[1] == '':
                        print('Missing quantity.')
                        break
                    else:
                        print('Invalid quantity.')
                        break
                x += 1
        elif len(cheese_amount) == 1 and cheese_amount[0] == 'back':
            return (gold_spent, tuple(cheese_bought))
        # the loop runs three times when the input is not cheese type.
        # while loop checks if the cheese_amount[0] matches
        # any of the first elements in tuples of CHEESE_MENU
        i = 0
        found = False
        while i < len(CHEESE_MENU) and not found:
            if cheese_amount[0] == CHEESE_MENU[i][0].lower():
                found = True
            i += 1
        if found:
            continue
        else:
            print(f"We don't sell {cheese_amount[0]}!")


def display_inventory(gold: int, cheese: list, trap: str) -> None:
    '''
    Displays contents of inventory.
    Parameters:
        gold:   int,  amount of gold that player has
        cheese: list, amount of each type of cheese that player has
        trap:   str,  name of trap that player that player has
    '''
    print(f'Gold - {gold}')
    w = 0
    while w < len(cheese):
        print(f'{cheese[w][0]} - {cheese[w][1]}')
        w += 1
    print(f'Trap - {trap}')


def main():
    choice = 0
    gold = 125
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    trap = 'Cardboard and Hook Trap'
    print('Welcome to The Cheese Shop!')
    o = 0 
    while o < len(CHEESE_MENU):
        print(f'{CHEESE_MENU[o][0]} - {CHEESE_MENU[o][1]} gold')
        o += 1
    while choice != '3':
        help_ye = ('\nHow can I help ye?\n1. Buy cheese'
                   '\n2. View inventory\n3. Leave shop\n')
        choice = (input(help_ye))
        if choice == '1':
            # gold_spent is the first element
            # of the returning tuple of buy_cheese(gold)
            # cheese_bought is the second element.
            gold_spent, cheese_bought = buy_cheese(gold)
            gold -= gold_spent
            i = 0
            while i < len(cheese):
                cheese[i][1] += cheese_bought[i]
                i += 1
        elif choice == '2':
            display_inventory(gold, cheese, trap)


if __name__ == "__main__":
    main()