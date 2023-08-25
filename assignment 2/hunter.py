'''
Write your solution for the class Hunter here.
This is your answer for Question 8.2.

Author:Minjae Kim
SID:5300094978
Unikey:mkim9138
'''
from trap import Trap
from name import is_valid_name, generate_name


class Hunter:
    def __init__(self):
        self.name = 'Bob'
        self.cheese = (["Cheddar", 0], ["Marble", 0], ["Swiss", 0])
        self.trap = Trap.get_trap_name
        self.gold = 125
        self.points = 0

    def set_name(self, player_name):
        if is_valid_name(player_name):
            self.name = player_name
        else:
            player_name = generate_name(player_name)
            self.name = player_name

    def set_cheese(self, quantity):
        if isinstance(quantity, tuple):
            self.cheese = quantity

    def set_gold(self, gold):
        if isinstance(gold, int):
            self.gold = gold

    def set_points(self, points):
        if isinstance(points, int):
            self.points = points

    def get_name(self):
        return self.name

    def get_cheese(self):
        i = 0
        cheese_ = ''
        while i < len(self.cheese):
            cheese_ += f'{self.cheese[i][0]} - {self.cheese[i][1]}\n'

    def get_gold(self):
        return self.gold

    def get_points(self):
        return self.points

    def update_cheese(self, quantity):
        if isinstance(quantity, tuple):
            a = 1
            while a < len(quantity):
                self.cheese[a][1] += quantity[a][1]
                a += 1
    def consume_cheese(self, Trap.trap_cheese):
        i = 0
        while i < len(self.cheese):
            if Trap.trap_cheese == self.cheese[i][0]:
                self.cheese[i][1] -= 1
            i += 1
    
    def have_cheese(self, Trap.trap_cheese='Cheddar'):
        i = 0
        while i < len(self.cheese):
            if Trap.trap_cheese == self.cheese[i][0]:
                return self.cheese[i][1]
            i += 1
        if not isinstance(Trap.trap_cheese, str):
            return 0
    
    def display_inventory(self):
        inventory = f'Gold - {self.gold}\n'
        i = 0
        while i < len(self.cheese):
            inventory += f'{self.cheese[i][0]} - {self.cheese[i][1]}\n'
            i += 1 
        inventory += f'Trap - {Trap.trap_name}\n'
        return inventory

    def arm_trap(self, cheese_name):
        i = 0
        while i < len(self.cheese):
            if self.cheese[i][0] == cheese_name and self.cheese[i][1] > 0:
                Trap.trap_cheese = cheese_name
                return
            i += 1
        if i == len(self.cheese):
            Trap.trap_cheese = None
            
    def update_gold(self, gold):
        if isinstance(gold, int):
            self.gold += gold
    
    def update_points(self, points):
        if isinstance(points, int):
            self.points += points
        
    def __str__(self):
        return f'''
{self.name}
Gold - {self.gold}
{self.display_inventory()}
'''