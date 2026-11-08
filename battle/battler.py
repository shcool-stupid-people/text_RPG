import random
import time
import questionary
from questionary import Choice
from player.resource import skill

class Entity_battler: # 플레이어와 적 담당자에게 스크립트(대사)를 반환하는 함수를 요청
    '''전투 시 생성하여 전투를 지속하는 객체(한 엔티티 당 하나)'''
    def __init__(self, obj, disruption):
        self.obj = obj
        self.disruption = disruption
        self.additional_turn = False

    def action(self, player, battler_groups):
        '''여기서 입력받는건 전부 베틀러임'''
        if(self.is_death()):
            return

    def attack(self, target, damage):
        print(f"{self.obj.get_name()}은(는) {target.obj.get_name()}을(를) 공격했다.")
        # 명중률 구현
        rand = random.randint(1, 100)
        if (rand <= self.get_accuracy()):
            target.on_hit(damage)
            # 체력이 음수로 표시되지 않도록 함
            my_hp = max(self.get_hp(), 0) 
            target_hp = max(target.get_hp(), 0)
            print(
                "[정보]: ",
                f"{self.obj.get_name()}의 체력: {my_hp}, "
                f"{target.obj.get_name()}의 체력: {target_hp}\n"
            )
            if (target.is_death()):
                print(f"{target.obj.get_name()}이(가) 죽었습니다.")
                self.disruption.exit_battle()
        else:
            print(f"...그러나 {self.obj.get_name()}의 공격은 빗나갔다.")
        
    def on_hit(self, damage):
        self.obj.on_hit(damage)

    def is_death(self):
        return self.obj.is_death()

    def get_attack_power(self):
        return self.obj.attack_power
    
    def get_hp(self):
        return self.obj.hp
    def get_accuracy(self):
        return self.obj.accuracy

class Monster_battler(Entity_battler):
    def action(self, player, battler_groups):
        if (self.is_death()): 
            print(f"{self.obj.get_name()}은(는) 싸울 수 있는 상태가 아니다.")
            self.disruption.exit_battle()
            return
        target = player
        # rand = random.randint(120, 200)
        # time.sleep(rand/100)
        skill = self.get_skill()
        print(f"{self.obj.name}은(는) {skill["name"]}을(를) 시전했다!")
        self.attack(target, skill["damage"])

    def get_skill(self):
        return self.obj.use_skill()
    
    def on_hit(self, damage):
        self.obj.take_damage(damage)

    def is_death(self):
        return not(self.obj.is_alive())

    def get_attack_power(self):
        return self.obj.get_damage()
    
    def get_hp(self):
        return self.obj.get_hp()
    
    def get_accuracy(self):
        return self.obj.get_accuracy()

class Player_battler(Entity_battler):
    def action(self, player, battler_groups):
        if (self.is_death()): 
            print(f"{self.obj.get_name()}은(는) 싸우기엔 체력이 충분하지 않다!")
            self.disruption.exit_battle()
            return
        
        # answer = int(input("1. 공격한다.\n2. 가만히 있는다.\n:"))
        # if answer == 1:
            
        #     self.attack(battler_groups[answer])
        actions = (
            "공격",
            # "적 분석하기",
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
        myskill = self.select_skill()
        if (myskill == 0): # 기본 공격을 선택하면
            damage = self.get_attack_power()
        elif (isinstance(myskill, skill.Attack_skill)):
            print(f"{self.obj.name}은(는) {myskill.get_name()}을(를) 사용했다!")
            damage = myskill.get_damage()

        elif (isinstance(myskill, skill.Effect_skill)):
            print(f"{self.obj.name}은(는) 대단한 {myskill.get_name()}을(를) 사용했다!")
            myskill.use_effect_skill(self.obj) # 플레이어
            return
        else:
            print(type(skill))
        target = self.select_target(battler_groups)
        self.attack(target, damage)

    def select_skill(self):
        skill_list = self.obj.get_skill()

        selection = []
        selection.append(Choice("기본 공격", 0))
        for i in range(len(skill_list)):
            selection.append(Choice(skill_list[i].get_name(), skill_list[i]))

        skill = questionary.select(
            "스킬을 선택하세요:",
            choices = selection
        ).ask()
        return skill

    def action_run(self):
        print(f"{self.obj.name}이(가) 도망쳤습니다.")
        self.disruption.exit_battle()


    def select_target(self, battler_groups) -> Entity_battler:
        selection = []
        for i in range(len(battler_groups)):
            selection.append(Choice(battler_groups[i].obj.name, i))

        targi_idx = questionary.rawselect(
            "타겟을 선택하세요[번호키 사용]:",
            choices = selection
        ).ask()
        # print(targi_idx)

        return battler_groups[targi_idx]

        
    def on_hit(self, damage):
        self.obj.change_hp(-damage)

    def is_death(self):
        return self.obj.get_hp() <= 0

    def get_attack_power(self):
        return self.obj.get_damage()
    
    def get_hp(self):
        return self.obj.get_hp()
    
    def get_accuracy(self):
        return self.obj.get_accuracy_rate()