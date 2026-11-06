# import battle.turnManager as turnManager
import enemy.enemy as enemy
# import enemy.enemy_manager as enemy_manager
# import enemy.resorce as resorce
import event.event as event
import battle.turn_manager as turn_manager
import player.resource.skill_manager as sk
import map.map as map
import player.player as player
# import shop.shop as shop
import questionary
import os
import random


#희찬이가 요청하는 사항
#1. 유통기한 이벤트가 있음. 즉 방 이동할때마다 수 하나가 차감되든 올라가든 함수 하나 만들어주기
class main():
    def __init__(self):
        #generate managers
        self.skill_manager = sk.skill_manager()
        #generate player
        self.a = player.player(self.skill_manager)
       
        #generate map
        self.world = map.field(self.a)
        
        #event_scheduler
        self.event_scheduer = []
        self.event_manager = event.event(self.a, self.world, self)

        #start
        self.main_loop()
    
    def main_loop(self):
        while(1):
            self.world.check_next_floor()
            self.world.show_map()
            self.choose_option()
            self.count_down_event_scheduer()

    def choose_option(self):
        self.check_grid = self.world.check_grid()
        
        option = questionary.select(
                message="선택하세요",
                choices=["이동하기", "인벤토리", "내 정보", "끝내기"]
            ).ask()
        # self.world.show_map()

        if (option == "이동하기"):
            self.player_move()
        elif (option == "인벤토리"):
            self.player_inventory()
        elif (option == "내 정보"):
            self.show_info()
        elif (option == "끝내기"):
            self.game_over()

    def game_over(self):
        print("게임이 종료되었습니다")
        os._exit(0)

    def player_move(self):
        # self.world.show_map()
        move = questionary.select(
            message="이동 선택하세요",
            choices=self.check_grid
        ).ask()

        if (move == "exit"):
            pass
        elif (move == "right"):
            self.a.move(1,0)
        elif (move == "left"):
            self.a.move(-1,0)
        elif (move == "up"):
            self.a.move(0,-1)
        elif (move == "down"):
            self.a.move(0,1)

        self.event_manager.drawing_event()
        self.world.check_room()


    def player_inventory(self):
        inv = self.a.open_inventory()

        choices = [
                questionary.Choice(
                    title=f"{item.name} (수량: {count}개)",
                    value=item
                )
                for item, count in inv.items()
            ]
        
        choices.append("취소/나가기")

        option = questionary.select(
                message="inventory",
                choices=choices
            ).ask()

        if (option == "취소/나가기"):
            pass

        else:
            cat = option.category
            if (cat == "무기"):
                print("무기를 장착했습니다")
                self.a.change_epuip_weapon(option)
            elif (cat == "방어구"):
                print("방어구를 장착했습니다")
                self.a.change_epuip_armor(option)
            elif (cat == "포션"):
                print("아이템을 사용했습니다")
                option.use_item()
                self.a.del_inventory(option)
                
    def add_event_scheduer(self, name, value):
        self.event_scheduer.append([name, value, 5])

    def count_down_event_scheduer(self):
        for i in range(len(self.event_scheduer)):
            self.event_scheduer[i][-1] -= 1
            if (self.event_scheduer[0][-1] == 0):
                self.del_effect(self.event_scheduer[i][0], self.event_scheduer[i][1])
                self.event_scheduer.remove(self.event_scheduer[i])
    
    def del_effect(self, name, v):
        if (name == "체력"):
            self.a.change_hp(-v)
        elif (name == "방어력"):
            self.a.change_armored(-v)
        elif (name == "마나"):
            self.a.change_mp(-v)
        elif (name == "스피드"):
            self.a.change_speed(-v)
        elif (name == "명중률"):
            self.a.change_accuracy_rate(-v)
        elif (name == "공격력"):
            self.a.change_damage(-v)
        
        
    def show_info(self):
        print(f"health: [{self.a.get_hp()}/{self.a.get_max_hp()}]")
        print(f"mp: [{self.a.get_mp()}/{self.a.get_max_mp()}]")
        print(f"damage: {self.a.get_damage()}")
        print(f"accuaracy: {self.a.get_accuracy_rate()}")
        print(f"coin: {self.a.get_coin()}")
        print(f"weapon: {self.a.get_equip_weapon()}")
        print(f"armor: {self.a.get_equip_armor()}")
        print(f"skill: {self.a.get_skill()}")


main()