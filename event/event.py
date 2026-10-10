import random
import player

class event():
    def __init__(self):
        self.status_event_list = [["hp","체력"], ["dex","방어력"], ["mp","마나"], ["spd","스피드"], ["acr","명중률"], ["atk","공격력"]]
        self.status_percent_list = [10,20,30,-10,-20,-30] #일시
        self.status_const_percent_list = [5,10,15,-5,-10,-15] #고정
        self.equipment_lv_list = [2,1,-1,-2] #등급
        self.equipment_reinforce_percent_list = [100,50,-50,-100] #강화확률
        self.equipment_money = [100,50,-50,-100] #강화 비용
        self.special_list = ["invincible","double_spawn","reset_all_buff"] #스페셜이벤트
        self.player = player.player() #플레이어 호출

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
        stat = random.choice(self.status_event_list)
        choice = random.randrange(0,2)
        if (choice == 0):
            value1 = random.choice(self.status_const_percent_list)
            self.player.change_hp(value1)
            print(f"{stat}가 영구적으로 {value1} 되었습니다.")

        else:
            value2 = random.choice(self.status_percent_list)
            self.player.change_hp(value2)
            print(f"{stat}가 일시적으로 {value2} 되었습니다.")
            #방 이동 만든 후 복구 하는 함수 호출하기
        
    def equipment_reinforce(self):
        result = random.randrange(0,3)
        if (result == 0):
            rank = random.choice(self.equipment_lv_list) #등급 호출
            #장비 관련 함수 추가 만들기
            print(f"장비 등급이 {rank}만큼 변화되었습니다.")
        elif (result == 1):
            percent = random.choice(self.equipment_reinforce_percent_list) #강화 확률 호출
            #장비 관련 함수 추가 만들기
            print(f"장비가 {percent}확률만큼 조정됩니다.")
        else:
            price = random.choice(self.equipment_money) #강화 비용 호출
            #장비 관련 함수 추가 만들기
            print(f"강화 비용이 {price}% 조정됩니다.")

    def special_event(self): 
        result = random.choice(self.special_list)
        if (result == "invincible"):
            print("무적 상태")
            #방 이동이 몇번 이루어지면
            print("무적 해제")
        elif (result == "double_spawn"):
            print("몹 2배 스폰!!")
        else:
            print("모든 버프 및 디버프 삭제")


    def soft_reset(self):
        pass #맵 나와야 제작 가능

    def hard_reset(self):
        pass #맵 나와야 제작 가능

test = event()
test.drawing_event()