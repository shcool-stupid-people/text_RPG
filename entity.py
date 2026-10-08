import random
import time


class Being:
    name = ''
    max_hp = 10
    hp = 0
    defense = 0
    attack_power = 1
    evasion = 0.0
    

    def __init__(self, hp = max_hp):
        if 0 <= hp <= self.max_hp:
            self.hp = hp
        else:
            print("[sys]: 범위에 맞지 않는 hp입니다.")

    def __str__(self):
        return f"{self.name}의 체력: {self.hp}/{self.max_hp}"
    
    def attack(self, target):
        print(f"{self.name}이(는) {target.name}을(를) 공격했다.")
        target.on_hit(self.attack_power)
        print(f"{self.name}의 체력: {self.hp}, {target.name}의 체력: {target.hp}\n")

    def on_hit(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.on_death()

    def on_death(self):
            print(f"{self.name}이(가) 죽었습니다.")

    def is_death(self):
        print(self.hp, self.hp <= 0)
        return self.hp <= 0



class Monster(Being):
    name = '몬스터'

class Player(Being):
    name="홍길동"
    attack_power = 5


if __name__ == "__main__":
    player = Player()
    player.name = input("플레이어의 이름을 입력하세요: ")
    monsert = Monster()

    print(f"야생의 {monsert.name}이(가) 나타났다!")
    while True:
        answer = int(input("1. 공격한다.\n2. 가만히 있는다.\n:"))
        if answer == 1:
            player.attack(monsert)
            print(monsert)

        monsert.attack(player)
        print(player)