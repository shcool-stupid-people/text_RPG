# 플레이어 행동과 죽는거 만들기(action을 못 하도록)

import entity  # noqa: F401, I001
import random
import time
import questionary
from questionary import Choice

class EntityBattler: # 플레이어와 적 담당자에게 스크립트(대사)를 반환하는 함수를 요청
    '''전투 시 생성하여 전투를 지속하는 객체(한 엔티티 당 하나)'''
    
    def __init__(self, obj, disruption):
        self.obj = obj
        self.disruption = disruption
        self.additional_turn = False

    def action(self, player, battler_groups):
        '''여기서 입력받는건 전부 베틀러임'''
        if(self.is_death()):
            return
    # def attack(self, target_battler):
    #     self.obj.attack(target_battler.obj)

    def attack(self, target, damage):
        print(f"{self.obj.name}이(는) {target.obj.name}을(를) 공격했다.")
        target.on_hit(damage)
        print(
            f"{self.obj.name}의 체력: {self.obj.hp}, "
            f"{target.obj.name}의 체력: {target.obj.hp}\n"
        )
        
    def on_hit(self, damage):
        self.obj.on_hit(damage)
        if (self.is_death()):
            self.disruption.exit_battle()

    def on_death(self):
        self.obj.on_death()

    def is_death(self):
        return self.obj.is_death()

    def get_attack_power(self):
        return self.obj.attack_power

class MonsterBattler(EntityBattler):
    def action(self, player, battler_groups):
        if (self.is_death()): 
            return
        target = player
        rand = random.randint(120, 200)
        time.sleep(rand/100)
        self.attack(target, self.get_attack_power())

class PlayerBattler(EntityBattler):
    def action(self, player, battler_groups):
        if (self.is_death()): 
            return
        
        # answer = int(input("1. 공격한다.\n2. 가만히 있는다.\n:"))
        # if answer == 1:
            
        #     self.attack(battler_groups[answer])
        actions = (
            "공격",
            "도망"
        )

        select = questionary.select(
            "행동을 선택하세요:",
            choices=actions
        ).ask()

        if select == "공격":
            self.action_attack(battler_groups)
        elif select == "도망":
            self.action_run()

    def action_attack(self, battler_groups):
        target = self.select_target(battler_groups)
        damage = self.get_attack_power()
        self.attack(target, damage)

    def action_run(self):
        print(f"{self.obj.name}이(가) 도망쳤습니다.")
        self.disruption.exit_battle()


    def select_target(self, battler_groups) -> EntityBattler:
        selection = []
        for i in range(len(battler_groups)):
            selection.append(Choice(battler_groups[i].obj.name, i))

        targi_idx = questionary.rawselect(
            "타겟을 선택하세요:",
            choices = selection
        ).ask()
        # print(targi_idx)

        return battler_groups[targi_idx]