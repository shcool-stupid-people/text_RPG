import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent)) # main.py기준으로 import하는 것이 호환되도록

from player import player
from battle import battler
from battle import entity
from player.resource import skill_manager
import random 
import time

class battle_disruption():
    ''' 중간 연결자 역활을 하는 클래스
    main코드는 이거를 조건으로 사용하여 중단을 시킴 
    entityBattler는 중단 신호를 발생시킴'''

    exit = False
    def __init__(self):
        self.exit = False

    def exit_battle(self):
        self.exit = True
        
    def is_exit(self):
        return self.exit


class TurnManager:

    def __init__(self, player):
        '''groups는 
        ((entity.being, entity.being, ...), 
        (entity.being, ...), 
        ..)
        의 형식으로 사용''' 

        self.turn_flow = []
        self.cnt = 1
        self.disruption = battle_disruption()
        
        self.player = player
        self.player_battler = battler.PlayerBattler(player, self.disruption)
        self.monsters = []


    def next_turn(self):
        if (not self.turn_flow) :
            self.turn_delay(0.05)
            print(f"---제 {self.cnt}턴---")
            self.set_turn_flow()

            self.cnt += 1
        battler = self.turn_flow.pop(0)
        self.turn_process(battler)
        

    def set_turn_flow(self):
        self.turn_flow.append(self.player_battler)
        for i in self.monsters.copy():
            self.turn_flow.append(i)
        # 추가 턴을 넣고 싶으면 여기에

    def turn_process(self, battler):
        battler.action(self.player_battler, self.monsters)


        
    def add_monster(self, monster):
        monsterBattler = battler.MonsterBattler(monster, self.disruption)
        self.monsters.append(monsterBattler)

    def turn_delay(self, delay_time=0.5):
        for i in range(2):
            print()
            # rand = random.randint(20, 100)
            # time.sleep(rand/100)
            time.sleep(delay_time)
        # rand = random.randint(20, 100)
        # time.sleep(rand/100)
        time.sleep(delay_time*1.2)


if __name__ == "__main__":
    skill_manager1 = skill_manager.skill_manager()
    user = player.player(skill_manager1)
    user.name = "홍길동"
    # player.name = input("플레이어의 이름을 입력하세요: ")
    monster = entity.Monster()
    monster.attack_power = 60 # 임시

    turn_manager = TurnManager(user)
    turn_manager.add_monster(monster)

    while True:
        turn_manager.next_turn()
        if (turn_manager.disruption.is_exit()):
            break
    print("끝남")
