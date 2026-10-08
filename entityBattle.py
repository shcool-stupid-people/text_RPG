# 플레이어 행동과 죽는거 만들기(action을 못 하도록)

import entity  # noqa: F401, I001
import random
import time

class EntityBattler: # 플레이어와 적 담당자에게 스크립트(대사)를 반환하는 함수를 요청
    '''전투 시 생성하여 전투를 지속하는 객체(한 엔티티 당 하나)'''
    
    def __init__(self, obj, disruption):
        self.obj = obj
        self.additional_turn = False

    def action(self, player, battler_groups):
        if(self.is_death()):
            return

    def on_hit(self, damage):
        self.obj.on_hit(damage)

    def on_death(self): # 안 사용할지도
        self.obj.on_death()

    def is_death(self):
        return self.obj.is_death()

class MonsterBattler(EntityBattler):
    def action(self, player, battler_groups):
        if (self.is_death()): 
            return
        target = player
        rand = random.randint(120, 200)
        time.sleep(rand/100)
        self.obj.attack(target.obj)

class PlayerBattler(EntityBattler):
    def action(self, player, battler_groups):
        if (self.is_death()): 
            return
        print("무언갈 함")
        # answer = int(input("1. 공격한다.\n2. 가만히 있는다.\n:"))
        # if answer == 1:
        #     print("무엇을 공격할까?")
        #     for i in range(len(OtherGroup)):
        #         print(f"{i}: {OtherGroup[i].name}")
        #     answer = int(input(": "))
        #     self.attack(OtherGroup[answer])