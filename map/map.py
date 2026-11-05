import random

class field():
    def __init__(self, player, shop):
        self.player = player
        self.shop = shop

        self.right_able = None
        self.left_able = None
        self.up_able = None
        self.down_able = None

        self.grid = [
                    [5, 5, 5, 5, 5, 5],
                    [5, 0, 0, 0, 0, 5],
                    [5, 0, 0, 0, 0, 5],
                    [1, 0, 0, 0, 0, 5],
                    [5, 0, 0, 0, 0, 5],
                    [5, 0, 0, 0, 0, 5],
                    [5, 5, 5, 5, 5, 5],
                    ]
        self.room_type = ["battle", "shop"]
        self.room = {}
        self.enterance = [3,0]
        self.generate_room()

    def show_map(self):
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

    def generate_room(self):
        room_num = random.randint(10, len(self.grid)*len(self.grid[0]) - (len(self.grid[0]) + len(self.grid))*2)

        for i in range(room_num):
            room_rand_x = random.randint(1,len(self.grid[0])-1)
            room_rand_y = random.randint(1,len(self.grid)-1)
            self.room[(room_rand_y, room_rand_x)] = random.choices(self.room_type, weights=[0.8, 0.2])[0] #need to fix same room can exist
    
    def get_enterance(self):
        return self.enterance
    
    def check_room(self):
        pos_r = self.player.get_pos()
        x = pos_r[1]
        y = pos_r[0]

        pos = (x, y)

        if (tuple(pos) in self.room.keys()):
            if(self.room[pos] == "battle" and self.grid[y][x] == 0):
                print("battle")
            elif(self.room[pos] == "shop"):
                print("상점을 발견했습니다")
                self.shop.shop1()

        if (self.grid[y][x] == 0):
            self.grid[y][x] = 2
            
    # def chanage(self):
    #     self.x = self.player.get_pos()
    #     self.y = self.player.get_pos()

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
