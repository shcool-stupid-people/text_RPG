import random

class event():
    def __init__(self,player, map, main):
        self.status_event_list = [["hp","체력"], ["dex","방어력"], ["mp","마나"], ["spd","스피드"], ["acr","명중률"], ["atk","공격력"]]
        self.status_percent_list = [10,20,30,-10,-20,-30] #일시
        self.status_const_percent_list = [5,10,15,-5,-10,-15] #고정
        self.equipment_lv_list = [2,1,-1,-2] #등급
        self.equipment_reinforce_percent_list = [100,50,-50,-100] #강화확률
        self.equipment_money = [100,50,-50,-100] #강화 비용
        self.special_list = ["invincible","double_spawn","reset_all_buff"] #스페셜이벤트
        self.player = player
        self.map = map
        self.main = main

    def drawing_event(self): #뽑기
        result = random.randrange(0,10000)
        if (result < 10):
            self.soft_reset()
        elif (result < 15):
            self.hard_reset()
        else:
            result2 = random.randrange(0,3)
            if (result2 == 0):
                self.status_exchange()
            elif (result2 == 1):
                self.equipment_reinforce()
            elif (result2 == 2):
                self.special_event()

    def status_exchange(self):
        stat = random.randrange(0,6) #0 = 체력, 1 = 방어력, 2= 마나, 3 = 스피드, 4 = 명중률, 5 = 공격력 
        choice = random.randrange(0,2)
        value1 = random.choice(self.status_const_percent_list)
        value2 = random.choice(self.status_percent_list)

        if (stat == 0): #체력
            if (choice == 0): 
                self.player.change_max_hp(value1)
                self.player.change_hp(value1)
                print(f"체력이 영구적으로 {value1}만큼 변동 되었습니다.") 

            else:
                self.player.change_hp(value2)
                self.player.change_max_hp(value2)
                self.main.add_event_scheduer("체력", value2)
                print(f"체력이 일시적으로 {value2}만큼 변동 되었습니다.")

        elif (stat == 1): #방어력
            if (choice == 0):
                self.player.change_armored(value1)
                print(f"방어력이 영구적으로 {value1}만큼 변동 되었습니다.") 

            else:
                self.player.change_armored(value2)
                self.main.add_event_scheduer("방어력", value2)
                print(f"방어력이 일시적으로 {value2}만큼 변동 되었습니다.")

        elif (stat == 2): #마나
            if (choice == 0):
                self.player.change_mp(value1)
                self.player.change_max_mp(value1)
                print(f"마나가 영구적으로 {value1}만큼 변동 되었습니다.") 
        
            else:
                self.player.change_max_mp(value2)
                self.player.change_mp(value2)
                self.main.add_event_scheduer("마나", value2)
                print(f"마나가 일시적으로 {value2}만큼 변동 되었습니다.")

        elif (stat == 3): #스피드
            if (choice == 0):
                self.player.change_speed(value1)
                print(f"스피드가 영구적으로 {value1}만큼 변동 되었습니다.") 
        
            else:
                self.player.change_speed(value2)
                self.main.add_event_scheduer("스피드", value2)
                print(f"스피드가 일시적으로 {value2}만큼 변동 되었습니다.")

        elif (stat == 4): #명중률
            if (choice == 0):
                self.player.change_accuracy_rate(value1)
                print(f"명중률이 영구적으로 {value1}만큼 변동 되었습니다.") 
        
            else:
                self.player.change_accuracy_rate(value2)
                self.main.add_event_scheduer("명중률", value2)
                print(f"명중률이 일시적으로 {value2}만큼 변동 되었습니다.")

        elif (stat == 5): #공격력
            if (choice == 0):
                self.player.change_damage(0.1 * value1)
                print(f"공격력이 영구적으로 {0.1 * value1}만큼 변동 되었습니다.") 
        
            else:
                self.player.change_damage(0.1 * value2)
                self.main.add_event_scheduer("공격력", value2*0.1)
                print(f"공격력이 일시적으로 {0.1 * value2}만큼 변동 되었습니다.")
        
    def equipment_reinforce(self):
        result = random.randrange(0,3)

        if (result == 0):
            rank = random.choice(self.equipment_lv_list) #등급 호출
            key = self.player.open_inventory()
            item_list = list(key.keys())
            dice = random.randrange(0,len(key))
            item_list[dice].level += rank
            print(f"{item_list[dice].name}가 {rank}만큼 변동되었습니다.")
        # elif (result == 1):
        #     percent = random.choice(self.equipment_reinforce_percent_list) #강화 확률 호출
        #     #장비 관련 함수 추가 만들기
        #     print(f"장비가 {percent}확률만큼 조정됩니다.")
        # else:
        #     price = random.choice(self.equipment_money) #강화 비용 호출
        #     #장비 관련 함수 추가 만들기
        #     print(f"강화 비용이 {price}% 조정됩니다.")

    def special_event(self): 
        result = random.choice(self.special_list)
        if (result == "invincible"):
            print("무적 상태")
            self.main.add_event_scheduer("방어력", 500000)
            print("무적 해제")
        elif (result == "double_spawn"):
            print("몹 2배 스폰!!")
        else:
            print("모든 버프 및 디버프 삭제")


    def soft_reset(self):
        self.map.floor_reset()
        print("층 초기화")

    def hard_reset(self):  
        self.map.room_floor(1)
        self.player.change_floor(1)
        self.map.reset() #함수 미구현
        print("태초마을")        



# test = event()
# test.drawing_event()

