class player():
    def __init__(self):
        self.hp = 100
        self.mp = 100
        self.damage = 10
        self.armored = 10
        
        self.accuracy_rate = 100

        self.coin = 100

        self.equipment_weapon = None
        self.equipment_armor = None

        self.inventory = {}
        
        self.applicated_event = []

        self.position = [] #(y,x)

        self.skill = []

    def get_hp(self):
        return self.hp

    def change_hp(self, value):
        self.hp += value

    def get_mp(self):
        return self.mp
    
    def change_mp(self, value):
        self.mp += value

    def get_accuracy_rate(self):
        return self.accuracy_rate

    def change_accuracy_rate(self, value):
        self.accuracy_rate += value

    def get_equip_weapon(self):
        return self.equipment_weapon
    
    def get_equip_armor(self):
        return self.equipment_armor

    def change_epuipmet_weapon(self, value):
        self.equipment_weapon = value

    def change_epuip_armor(self, value):
        self.equipment_armor = value

    def add_event(self, event):
        self.applicated_event.append(event)

    def remove_event(self, event):
        self.applicated_event.remove(event)

    def get_player_pos(self):
        return self.position
    
    def change_player_pos(self, x, y):
        self.position[0] = y
        self.position[1] = x

    def get_coin(self):
        return self.coin

    def change_coin(self, value):
        self.coin += value

    def get_damage(self):
        real_damage = self.get_equip_weapon.get_damage() + self.damage #need to change/ how to get weapons damage
        return real_damage
    
    def change_damage(self, value):
        self.damage += value

    def get_armored(self):
        real_armored = self.get_equip_armor.get_damage() + self.armored #need to change/ how to get weapons damage
        return real_armored
    
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

    def add_inventory(self, item):
        if (item in self.inventory and not(item.get_category == "weapon")):  #need to fix
            self.inventory[item] += 1

        elif (item in self.inventory):
            self.inventory[item] += 1

        else:
            self.inventory[item] = 1

    def del_inventory(self, item):
        if (item in self.inventory and not(item.get_category == "weapon")):  #need to fix
            self.inventory[item] -= 1

        elif (item in self.inventory):
            self.inventory[item] -= 1

        else:
            print("item is not exist")

    def equip_skill(self):
        pass

    def unequip_skill(self):
        pass

    def use_skill(self):
        pass
