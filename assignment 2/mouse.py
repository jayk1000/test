'''
Write solutions to 3. New Mouse Release here.

Author:Minjae Kim
SID:530009478
Unikey:mkim9138
'''

'''
Keep this line!
'''
import random

TYPE_OF_MOUSE = (None, "Brown", "Field", "Grey", "White", "Tiny")
    

def generate_mouse() -> str | None:
    '''
    Spawn a random mouse during a hunt depending on cheese type
    Hint: You should be using TYPE_OF_MOUSE in this function.
    Returns:
        spawn_mouse: str | None, type of mouse
    '''
    random_mouse = random.random()
    if random_mouse < 0.5:
        spawn_mouse = TYPE_OF_MOUSE[0]
    elif random_mouse < 0.6:
        spawn_mouse = TYPE_OF_MOUSE[1]
    elif random_mouse < 0.75:
        spawn_mouse = TYPE_OF_MOUSE[2]
    elif random_mouse < 0.85:
        spawn_mouse = TYPE_OF_MOUSE[3]
    elif random_mouse < 0.95:
        spawn_mouse = TYPE_OF_MOUSE[4]
    else:
        spawn_mouse = TYPE_OF_MOUSE[5]
    return spawn_mouse


def loot_lut(mouse_type: str | None) -> tuple:
    '''
    Look-up-table for gold and points for different types of mouse
    Parameter:
        mouse_type: str | None, type of mouse
    Returns:
        gold:       int, amount of gold reward for mouse
        points:     int, amount of points given for mouse
    '''
    loot = {
        TYPE_OF_MOUSE[0]: (0, 0),
        TYPE_OF_MOUSE[1]: (125, 115),
        TYPE_OF_MOUSE[2]: (200, 200),
        TYPE_OF_MOUSE[3]: (125, 90),
        TYPE_OF_MOUSE[4]: (100, 70),
        TYPE_OF_MOUSE[5]: (900, 200)
    }
    i = 0
    while i < len(TYPE_OF_MOUSE):
        if TYPE_OF_MOUSE[i] == mouse_type:
            break
        i += 1
    return loot[TYPE_OF_MOUSE[i]]


class Mouse:
    def __init__(self):
        name = generate_mouse()
        self.name = name
        (self.gold, self.points) = loot_lut(name)

    def get_name(self) -> str:
        return self.name

    def get_gold(self) -> int:
        return self.gold

    def get_points(self) -> int:
        return self.points

    def __str__(self) -> str:
        return f"{self.name}"


def main():
    caught_mouse = Mouse()
    print(caught_mouse)


if __name__ == "__main__":
    main()
