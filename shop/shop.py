import questionary as qu
import random
import player
class shop():
    class item():
        def __init__(self, name, price):
            self.name = name
    class weapon(item):
        def __init__(self, name, price, damage):
            super().__init__(name, price)
            self.damage = damage
            self.Tear="일반"
            self.category = "무기"
            self.level = 1

    class armor(item):
        def __init__(self, name, price, defense):
            super().__init__(name, price)
            self.defense = defense
            self.Tear="일반"
            self.category = "방어구"
            self.level = 1

    class att_potion(item):
        def __init__(self, name, price, effect):
            super().__init__(name, price)
            self.effect = effect
            self.category = "포션"
            self.target="상대"

    class heal_potion(item):
        def __init__(self, name, price, effect):
            super().__init__(name, price)
            self.effect = effect
            self.category = "포션"
            self.target="자신"

    def __init__(self, a, b, coin):
        self.att_tool_name=[]
        self.att_tool_Lev=b
        self.money=coin

    def rainforce(self):
        while(1):     
            if self.att_tool_Lev==10:
                print("이미 최대 레벨입니다")
                return
            choices=qu.select(f"현재 무기는 {self.att_tool_Lev}레벨 입니다. 강화하겠습니까?\n강화 실패확률: {self.att_tool_Lev*10}%), 현재 잔액: {self.money}원", choices=["강화하기", "취소하기"]).ask()
            num=random.randrange(1, 100)
            if choices=="취소하기":
                print("강화를 종료합니다\n\n")
                return
            elif choices=="강화하기":
                if self.att_tool_Lev<=10:
                    if self.money<1000*self.att_tool_Lev:
                        print("돈이 부족합니다\n\n")
                    elif num>=self.att_tool_Lev*10+self.att_tool_Lev:
                        self.att_tool_Lev+=1
                        self.money -= 1000 * self.att_tool_Lev
                        print("강화에 성공하셨습니다\n\n")
                    elif num<=self.att_tool_Lev:
                        self.money -= 1000 * self.att_tool_Lev
                        self.att_tool_Lev=1
                        print("장비가 파괴되었습니다\n(그러니까 적당히 강화하라니까?)\n\n")
                    else:
                        self.money -= 1000 * self.att_tool_Lev
                        print("강화에 실패하셨습니다\n\n")

    def sell(self):
        while(1):
            choices=qu.select("판매할 아이템을 선택해주세요", choices=["무기", "방어구", "포션", "나가기"]).ask()
            if choices=="무기":
                print("무기를 판매합니다 (여기에서 판매되는 무기는 모두 )")
                choices=qu.select("판매할 아이템을 선택해주세요", choices=["마법지팡이", "검", "창", "나가기"]).ask()
            elif choices=="방어구":
                choices=qu.select("판매할 아이템을 선택해주세요", choices=[" 방패", "갑옷", "창", "나가기"]).ask()
                print("방어구를 판매합니다")
            elif choices=="포션":
                print("포션을 판매합니다")
            elif choices=="나가기":
                print("판매를 종료합니다")
                break

    def shop1(self):
        while(1): 
            choices=qu.select("상점에 오신 것을 환영합니다\n무엇을 하시겠습니까?", choices=["강화하기", "구매하기", "판매하기", "나가기"]).ask()
            if choices=="강화하기":
                self.rainforce()
            elif choices=="구매하기":
                print("구매하기를 선택하셨습니다")
            elif choices=="판매하기":
                print("판매하기를 선택하셨습니다")
            elif choices=="나가기":
                print("상점을 나갑니다")
                break
                                                                                                                                                    

if __name__ == "__main__":
    a=shop()
