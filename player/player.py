class player():
    def __init__(self, skill_manager):
        self.name = "player"

        self.hp = 100
        self.max_hp = 100
        self.mp = 100
        self.max_mp = 100
        self.damage = 10
        self.armored = 10
        self.speed = 100
        
        self.accuracy_rate = 100

        self.coin = 10000

        self.floor = 1

        self.equipment_weapon = None
        self.equipment_armor = None

        self.inventory = {}
        
        self.applicated_event = []

        self.position = [3, 0] #(y,x)

        self.skill_possess = []

        self.skill_manager = skill_manager
    
    def get_speed(self):
        return self.speed

    def change_speed(self, value):
        self.speed += value
    
    def get_name(self):
        return self.name
    
    def get_floor(self):
        return self.floor

    def change_floor(self, value):
        self.floor += value
        
    def get_hp(self):
        return self.hp

    def change_hp(self, value):
        self.hp += value
        if (self.max_hp < self.hp):
            self.hp = self.max_hp

    def get_max_hp(self):
        return self.max_hp

    def change_max_hp(self, value):
        self.max_hp += value

    def get_max_mp(self):
        return self.max_mp

    def change_max_mp(self, value):
        self.max_mp += value

    def get_mp(self):
        return self.mp
    
    def change_mp(self, value):
        self.mp += value
        if (self.max_mp < self.mp):
            self.mp = self.max_mp
    
    def get_accuracy_rate(self):
        return self.accuracy_rate

    def change_accuracy_rate(self, value):
        self.accuracy_rate += value

    def get_equip_weapon(self):
        return self.equipment_weapon
    
    def get_equip_armor(self):
        return self.equipment_armor

    def change_epuip_weapon(self, value):
        self.equipment_weapon = value

    def change_epuip_armor(self, value):
        self.equipment_armor = value

    def add_event(self, event):
        self.applicated_event.append(event)

    def remove_event(self, event):
        self.applicated_event.remove(event)

    def get_pos(self):
        return self.position
    
    def change_pos(self, x, y):
        self.position[0] = y
        self.position[1] = x
    
    def move(self, x, y):
        self.position[0] += y
        self.position[1] += x

    def get_coin(self):
        return self.coin

    def change_coin(self, value):
        self.coin += value

    def get_damage(self):
        try:
            real_damage = self.get_equip_weapon.get_damage() + self.damage #need to change/ how to get weapons damage
            return real_damage
        except:
            return self.damage
        
    def change_damage(self, value):
        self.damage += value

    def get_armored(self):
        try:
            real_armored = self.get_equip_armor.get_damage() + self.armored #need to change/ how to get weapons damage
            return real_armored
        except:
            return self.armored
        
    def change_armored(self, value):
        self.armored += value

    def on_damaged(self, damage):
        temp = self.armored - damage
        if(temp>0):
            pass
        else:
            self.change_hp(temp)
            
    def is_dead(self):
        if(self.hp <= 0):
            return True
        return False
        
    def open_inventory(self):
        return self.inventory

    def add_inventory(self, item, value=1):
        if (item in self.inventory and not(item.category == "weapon")):  #need to fix
            self.inventory[item] += value

        elif (item in self.inventory):
            self.inventory[item] += value

        else:
            self.inventory[item] = 1

    def del_inventory(self, item):
        # if (item in self.inventory and not(item.category == "weapon")):  #need to fix
        #     self.inventory[item] -= 1

        # elif (item in self.inventory):
        #     self.inventory[item] -= 1
        if (self.inventory[item] == 0):
            del self.inventory[item]
            
        if (item in self.inventory and not(item.category) == "포션"):
            del self.inventory[item]
        
        elif (item in self.inventory and self.inventory[item] != 0):
            self.inventory[item] -= 1
      
        else:
            print("item is not exist")
    def get_skill(self):
        return self.skill_possess
    
    def posses_skill(self, value):
        self.skill_possess.append(value)

    def use_skill(self, value):
        using_skill = self.skill_possess[value]
        return using_skill.get_name(), using_skill.get_mp()

#posses_skill를 불러와서 use_skill에 인덱스를 넘겨주는 형식으로 사용