# import battle.turnManager as turnManager
# import enemy.enemy as enemy
# import enemy.enemy_manager as enemy_manager
# import enemy.resorce as resorce
# import event.event as event
import player.resource.skill_manager as sk
import map.map as map
import player.player as player
import shop.shop as shop
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

        self.world = map.field(self.a)
        self.world.generate_room()

        #event_scheduler
        self.event_scheduer = {}

        #start
        self.main_loop()
    
    def main_loop(self):
        while(1):
            self.choose_option()

    def choose_option(self):
        self.check_grid = self.world.check_grid()
        
        option = questionary.select(
                message="선택하세요",
                choices=["이동하기", "인벤토리", "내 정보"]
            ).ask()
        if (option == "이동하기"):
            self.player_move()
        elif (option == "인벤토리"):
            self.player_inventory()
        elif (option == "내 정보"):
            self.show_info()

    def game_over(self):
        print("게임이 종료되었습니다")
        os._exit(0)

    def player_move(self):
        self.world.show_map()
        move = questionary.select(
            message="이동 선택하세요",
            choices=self.check_grid
        ).ask()

        if (move == "exit"):
            self.game_over()
        elif (move == "right"):
            self.a.move(1,0)
        elif (move == "left"):
            self.a.move(-1,0)
        elif (move == "up"):
            self.a.move(0,-1)
        elif (move == "down"):
            self.a.move(0,1)

        self.world.check_room()

    def player_inventory(self):
        inv = self.a.open_inventory()
        # inv = {"물약": 1, "칼": 1}

        choices = [
                questionary.Choice(
                    title=f"{item} (수량: {count}개)",
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
            cat = option.get_catagory()
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
                

    def show_info(self):
        pass



main()