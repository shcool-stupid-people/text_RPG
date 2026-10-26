import random

class field():
    def __init__(self, player):
        self.player = player

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
        
    def generate_room(self):
        room_num = random.randint(10, len(self.gird)*len(self.grid[0]) - (len(self.grid[0]) + len(self.grid))*2)

        for i in range(room_num):
            room_rand_x = random.randint(1,len(self.grid[0])-1)
            room_rand_y = random.randint(1,len(self.grid)-1)
            self.room[(room_rand_y, room_rand_x)] = random.choices(self.room_type, weights=[0.8, 0.2])[0] #need to fix same room can exist
    
    def get_enterance(self):
        return self.enterance
    
    def check_room(self):
        pos = self.player.get_pos()
        if (pos in self.room):
            if(self.room[pos] == "battle"):
                print("battle")
            elif(self.room[pos] == "shop"):
                print("shop")

    def check_grid(self):
        choies_options = ["exit"]

        self.check_right()
        self.check_left()
        self.check_up()
        self.check_down()

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

    def check_right(self):
        if (self.x+1 > len(self.grid[0]) or self.grid[self.y][self.x+1] == 5):
            self.right_able = False
        else:
            self.right_able = True

    def check_left(self):
        if (self.x-1 < 0) or self.grid[self.y][self.x-1] == 5:
            self.left_able = False
        else:
            self.left_able = True

    def check_up(self):
        if (self.y-1 < 0 or self.grid[self.y-1][self.x] == 5):
            self.up_able = False
        else:
            self.up_able = True

    def check_down(self):
        if (self.y+1 > len(self.grid[0]) or self.grid[self.y+1][self.x] == 5):
            self.down_able = False
        else:       
            self.down_able = True
