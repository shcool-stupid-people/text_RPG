import questionary as qu
import random
class shop():
    def __init__(self, a, b, coin):
        self.att_tool_name=a
        self.att_tool_Lev=b
        self.money=coin
    def rainforce(self):
        while(1):     
            if self.att_tool_Lev==10:
                print("이미 최대 레벨입니다")
                return
            choices=qu.select(f"현재 무기는 {self.att_tool_Lev}레벨 입니다. 강화하겠습니까?\n강화 실패확률: {self.att_tool_Lev*10}%)", choices=["강화하기", "취소하기"]).ask()
            num=random.randrange(1, 100)
            if choices=="취소하기":
                print("강화를 종료합니다")
                return
            elif choices=="강화하기":
                if self.att_tool_Lev<=10:
                    if num>=self.att_tool_Lev*10:
                        self.att_tool_Lev+=1
                        print("강화에 성공하셨습니다")
                    elif num<=self.att_tool_Lev*10:
                        print("강화에 실패하셨습니다")
                    elif num<=self.att_tool_Lev:
                        self.att_tool_Lev=1
                        print("장비가 파괴되었습니다\n(그러니까 적당히 강화하라니까?)\n")
    def shop1(self):
        while(1): 
            choices=qu.select("상점에 오신 것을 환영합니다\n무엇을 하시겠습니까?", choices=["강화하기", "나가기"]).ask()
            if choices=="강화하기":
                self.rainforce()
            elif choices=="나가기":
                print("상점을 나갑니다")
                break
a=shop("활", 5, 100000)
a.shop1()