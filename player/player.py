class player():
    def __init__(self):
        self.hp = 100
        self.mp = 100
        self.damage = 10
        self.accuracy_rate = 100

        self.equipment = None
        self.inventory = []
        
        self.applicated_event = []

        self.position = []


    def get_hp(self):
        return self.hp

    def change_hp(self, hp):
        self.hp += hp

    def get_mp(self):
        return self.mp
    
    def change_mp(self, mp):
        self.mp += mp
    
    def get_damage(self):
        return self.damage
    
    def change_damage(self, damage):
        self.damage += damage

    def get_accuracy_rate(self):
        return self.accuracy_rate

    def change_accuracy_rate(self, acc):
        self.accuracy_rate += acc

    def get_equip(self):
        return self.equipment

    def change_epuip(self, equip):
        self.equipment = equip

    def open_inventory(self):
        pass

    def add_event(self, event):
        self.applicated_event.append(event)

    def remove_event(self, event):
        self.applicated_event.remove(event)

    def get_player_postion(self):
        return self.position
    
    def change_player_postion(self, x, y):
        self.position[0] = x
        self.position[1] = y