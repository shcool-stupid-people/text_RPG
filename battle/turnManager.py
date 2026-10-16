import entity  # noqa: I001
# from ..player import player
import random  # noqa: F401
import time
import entityBattle

class BattleDisruption:
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
        self.disruption = BattleDisruption()
        
        self.player = player
        self.player_battler = entityBattle.PlayerBattler(player, self.disruption)
        self.monsters = []


    def next_turn(self):
        if (self.turn_flow) :
            battler = self.turn_flow.pop(0)
            self.turn_process(battler)
        else:
            self.turn_delay(0.05)
            print(f"---제 {self.cnt}턴---")
            self.set_turn_flow()

            self.cnt += 1

    def set_turn_flow(self):
        self.turn_flow.append(self.player_battler)
        for i in self.monsters.copy():
            self.turn_flow.append(i)
        # 추가 턴을 넣고 싶으면 여기에

    def turn_process(self, battler):
        battler.action(self.player_battler, self.monsters)


        
    def add_monster(self, monster):
        monsterBattler = entityBattle.MonsterBattler(monster, self.disruption)
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
    import sys
    import os

    # 1. 현재 파일(main.py)의 절대 경로의 상위 폴더(parent_folder) 경로를 계산합니다.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)

    # 2. 상위 폴더 안에 있는 가져오고 싶은 특정 폴더(uncle_folder)의 경로를 만듭니다.
    target_dir = os.path.join(parent_dir, 'player')

    # 3. 파이썬이 모듈을 찾을 수 있도록 검색 경로(sys.path)에 추가합니다.
    if target_dir not in sys.path:
        sys.path.append(target_dir)

    # 4. 이제 폴더 안의 파일을 자유롭게 임포트할 수 있습니다.
    import player
    # 또는 from my_module import my_function
    user = player.player()
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
