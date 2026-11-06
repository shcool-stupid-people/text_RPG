import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent)) # main.py기준으로 import하는 것이 호환되도록

import random
import enemy.enemy_manager as enemy_manager
import shop.shop as shop
import battle.turn_manager as turn_manager

class field():
    def __init__(self, player):
        self.player = player

        self.right_able = None
        self.left_able = None
        self.up_able = None
        self.down_able = None
        
        self.grid = None
        
        self.map1 = [
                    [5, 5, 5, 5, 5, 5],
                    [5, 0, 0, 0, 0, 5],
                    [5, 0, 0, 0, 0, 5],
                    [1, 0, 0, 0, 0, 5],
                    [5, 0, 0, 0, 0, 5],
                    [5, 0, 0, 0, 0, 5],
                    [5, 5, 5, 5, 5, 5],
                    ]

        self.map2 = [
                    [5, 5, 5, 5, 5, 5],
                    [5, 0, 0, 0, 0, 5],
                    [5, 0, 0, 0, 0, 5],
                    [1, 0, 0, 0, 0, 5],
                    [5, 0, 0, 0, 0, 5],
                    [5, 0, 0, 0, 0, 5],
                    [5, 5, 5, 5, 5, 5],
                    ]


        self.map3 = [
                    [5, 5, 5, 5, 5, 5],
                    [5, 0, 0, 0, 0, 5],
                    [5, 0, 0, 0, 0, 5],
                    [1, 0, 0, 0, 0, 5],
                    [5, 0, 0, 0, 0, 5],
                    [5, 0, 0, 0, 0, 5],
                    [5, 5, 5, 5, 5, 5],
                    ]

        self.maps = [self.map1, self.map2, self.map3]
        
        self.room_type = ["battle", "shop"]
    
        self.room = [{},{},{}]
        self.room_floor(self.player.get_floor())

        self.enemy_manager = enemy_manager.enemy_manager()
        self.turn_manager = turn_manager.Turn_manager(self.player)

        self.shop = shop.shop(self.player)


    def show_map(self):
        # print(self.room[0])
        # print(self.room[1])
        # print(self.room[2])
        for i in range(len(self.grid)):
            for j in self.grid[i]:
                if (j == 5):
                    print("==", end="")
                elif (j == 0):
                    print("x", end="")
                elif (j == 2):
                    print("O", end="")
                else:
                    print(f"{j} ",end="")
            print()

    def find_enterence(self):
        for i in range(len(self.grid)):
            for j in self.grid[i]:
                if (j == 1):
                    return [i, j-1]
                    

    def room_floor(self, floor):
        self.grid = self.maps[floor-1]
        enterance = self.find_enterence()
        # print(enterance)
        self.player.change_pos(enterance[1], enterance[0])

        if (len(self.room[floor-1]) == 0):
            self.generate_room(floor-1)

    def generate_room(self, value):
        room_num = random.randint(10, len(self.grid)*len(self.grid[0]) - (len(self.grid[0]) + len(self.grid))*2)

        for i in range(room_num):
            room_rand_x = random.randint(1,len(self.grid[0])-1)
            room_rand_y = random.randint(1,len(self.grid)-1)
            self.room[value][(room_rand_y, room_rand_x)] = random.choices(self.room_type, weights=[0.8, 0.2])[0] #need to fix same room can exist

    def get_enterance(self):
        return self.enterance
    
    def check_room(self):
        pos_r = self.player.get_pos()
        x = pos_r[1]
        y = pos_r[0]

        pos = (x, y)

        if (pos in self.room[self.player.get_floor()-1].keys()):
            if(self.room[self.player.get_floor()-1][pos] == "battle" and self.grid[y][x] == 0):
                print("battle")
                self.battle_room()
            elif(self.room[self.player.get_floor()-1][pos] == "shop"):
                print("상점을 발견했습니다")
                self.shop.start_shop()

        if (self.grid[y][x] == 0):
            self.grid[y][x] = 2

    def battle_room(self):
        self.turn_manager.add_monster(self.enemy_manager.select_enemy(self.player.get_floor()))
        while (1):
            self.turn_manager.next_turn()
            if (self.turn_manager.disruption.is_exit()):
                break
        print("종료")


    def check_grid(self):
        pos = self.player.get_pos()

        choies_options = ["exit"]

        self.check_right(pos)
        self.check_left(pos)
        self.check_up(pos)
        self.check_down(pos)

        if (self.right_able):
            choies_options.append("right")

        if (self.left_able):
            choies_options.append("left")

        if (self.up_able):
            choies_options.append("up")

        if (self.down_able):
            choies_options.append("down")

        if (not(len(choies_options))):
            print("선택되지 않았습니다")

            return None
        
        return choies_options

    def check_right(self, pos):
        x = pos[1]
        y = pos[0]
        if (x+1 > len(self.grid[0]) or self.grid[y][x+1] == 5):
            self.right_able = False
        else:
            self.right_able = True

    def check_left(self, pos):
        x = pos[1]
        y = pos[0]
        if (x-1 < 0) or self.grid[y][x-1] == 5:
            self.left_able = False
        else:
            self.left_able = True

    def check_up(self, pos):
        x = pos[1]
        y = pos[0]
        if (y-1 < 0 or self.grid[y-1][x] == 5):
            self.up_able = False
        else:
            self.up_able = True

    def check_down(self, pos):
        x = pos[1]
        y = pos[0]
        if (y+1 > len(self.grid[0]) or self.grid[y+1][x] == 5):
            self.down_able = False
        else:       
            self.down_able = True
