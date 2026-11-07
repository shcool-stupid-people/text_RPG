class item:
    def __init__(self, name, price, tear):
        self.name = name
        self.price = price
        self.tear = tear

class weapon(item):
    def __init__(self, name, price, damage, tear="일반"):
        super().__init__(name, price, tear)
        self.damage = damage
        self.category = "무기"
        self.level = 1

class armor(item):
    def __init__(self, name, price, defense, tear="일반"):
        super().__init__(name, price, tear)
        self.defense = defense
        self.category = "방어구"
        self.level = 1

class att_potion(item):
    def __init__(self, name, price, effect, tear="일반"):
        super().__init__(name, price, tear)
        self.effect = effect
        self.category = "포션"
        self.target = "상대"

class heal_potion(item):
    def __init__(self, name, price, effect, tear="일반"):
        super().__init__(name, price, tear)
        self.effect = effect
        self.category = "포션"
        self.target = "자신"

    def use_item(self, player):
        player.change_hp(self.effect)

class mp_potion(item):
    def __init__(self, name, price, effect, tear="일반"):
        super().__init__(name, price, tear)
        self.effect = effect
        self.category = "포션"
        self.target = "자신"

    def use_item(self, player):
        player.change_hp(self.effect)
    

class shop_manager():
    def __init__(self):
        self.weapon_list = [
            weapon("마법지팡이", 1000, 10),
            weapon("검", 1000, 15),
            weapon("창", 1000, 20),
        ]
        
        self.armor_list = [
            armor("방패", 1000, 10),
            armor("갑옷", 1000, 20),
            armor("투구", 1000, 5),
        ]

        self.potion_list = [
            att_potion("공격포션", 1000, -20),
            att_potion("엄청난 공격포션", 2000, -40),
            heal_potion("회복포션", 1000, 20),
            heal_potion("엄청난 회복포션", 2000, 40),
            heal_potion("마나포션", 1000, 20),
            heal_potion("엄청난 마나포션", 2000, 40),
        ]
    def get_weapon_list(self):
        return self.weapon_list
    
    def get_armor_list(self):
        return self.armor_list
    
    def get_potion_list(self):
        return self.potion_list
            

