import random
import questionary as qu
import player

class shop:

  class item:

    def __init__(self, name, price, tear):
      self.name = name
      self.price = price
      self.tear = tear

  class weapon(item):

    def __init__(self, name, price, damage, tear="일반"):
      super().__init__(name, price, tear)
      self.damage = damage
      self.category = "무기"
      self.level = 1

  class armor(item):

    def __init__(self, name, price, defense, tear="일반"):
      super().__init__(name, price, tear)
      self.defense = defense
      self.category = "방어구"
      self.level = 1

  class att_potion(item):

    def __init__(self, name, price, effect, tear="일반"):
      super().__init__(name, price, tear)
      self.effect = effect
      self.category = "포션"
      self.target = "상대"

  class heal_potion(item):

    def __init__(self, name, price, effect, tear="일반"):
      super().__init__(name, price, tear)
      self.effect = effect
      self.category = "포션"
      self.target = "자신"

  def __init__(self, tool_name, tool_lev, coin, tear="일반"):
    self.att_tool_name = tool_name
    self.att_tool_Lev = tool_lev
    self.money = coin
    self.Tear = tear

    self.weapon_list = [
        self.weapon("마법지팡이", 1000, 10),
        self.weapon("검", 1000, 15),
        self.weapon("창", 1000, 20),
    ]
    self.defense_list = [
        self.armor("방패", 1000, 10),
        self.armor("갑옷", 1000, 20),
        self.armor("투구", 1000, 5),
    ]
    self.potion_list = [
        self.att_potion("공격포션", 1000, -20),
        self.att_potion("엄청난 공격포션", 2000, -40),
        self.heal_potion("회복포션", 1000, 20),
        self.heal_potion("엄청난 회복포션", 2000, 40),
    ]

  def rainforce(self):
    while True:
      plus=9 if self.Tear == "전설" else 7 if self.Tear == "영웅" else 5 if self.Tear == "일반" else 4
      if self.att_tool_Lev >= 10:
        choices = qu.select(
            "무기 승급에 도전하시겠습니까?", choices=["승급하기", "나가기"]
        ).ask()
        if choices == "승급하기":
          if self.Tear == "일반":
            choices = qu.select(
                f"{self.Tear}에서 희귀등급으로 강화하시겠습니까?\n강화 실패 확률: 40%, 무기 파괴확률: 4%",
                choices=["예", "아니요"],
            ).ask()
            if choices == "예":
              num = random.randrange(1, 100)
              if num <= 4:
                self.money -= 1000 * self.att_tool_Lev
                self.att_tool_Lev = 1
                print("장비갘 파괴되었습닠다ㅋ\n\n")
              elif num <= 40:
                self.money -= 1000 * self.att_tool_Lev
                print("승급에 실패하셨습니다\n\n")
              else:
                print("승급에 성공하였습니다\n\n")
                self.money -= 1000 * self.att_tool_Lev
                self.Tear = "희귀"
                self.att_tool_Lev=1

            elif self.Tear == "희귀":
                    choices = qu.select(
                        f"{self.Tear}에서 영웅등급으로 강화하시겠습니까?\n강화 실패 확률: 70%, 무기 파괴확률: 7%",
                        choices=["예", "아니요"],
                    ).ask()
                    if choices == "예":
                      num = random.randrange(1, 100)
                      if num <= 7:
                        self.money -= 1000 * self.att_tool_Lev
                        self.att_tool_Lev = 1
                        print("장비갘 파괴되었습닠다ㅋ\n\n")
                        self.Tear = "일반"
                      elif num <= 70:
                        self.money -= 1000 * self.att_tool_Lev
                        print("승급에 실패하셨습니다\n\n")
                      else:
                        print("승급에 성공하였습니다")
                        self.money -= 1000 * self.att_tool_Lev
                        self.Tear = "영웅"
                        self.att_tool_Lev=1

            elif self.Tear == "영웅":
                    choices = qu.select(
                        f"{self.Tear}에서 전설등급으로 강화하시겠습니까?\n강화 실패 확률: 90%, 무기 파괴확률: 9%",
                        choices=["예", "아니요"],
                    ).ask()
                    if choices == "예":
                      num = random.randrange(1, 100)
                      if num <= 9:
                        self.money -= 1000 * self.att_tool_Lev
                        self.att_tool_Lev = 1
                        print("장비갘 파괴되었습닠다ㅋ\n\n")
                        self.Tear = "희귀"
                      elif num <= 90:
                        self.money -= 1000 * self.att_tool_Lev
                        print("승급에 실패하셨습니다\n\n")
                      else:
                        print("승급에 성공하였습니다")
                        self.money -= 1000 * self.att_tool_Lev
                        self.Tear = "전설"
                        self.att_tool_Lev=1
            else:
              print("이미 최고 등급입니다")
        
      choices = qu.select(
          f"현재 무기는 {self.att_tool_Lev}레벨 입니다. 강화하겠습니까?\n강화 실패확률:"
          f" {self.att_tool_Lev*plus}%, 무기 파괴 확률: {self.att_tool_Lev}%, 현재"
          f" 잔액: {self.money}원",
          choices=["강화하기", "취소하기"],
      ).ask()
      num = random.randrange(1, 100)
      if choices == "취소하기":
        print("강화를 종료합니다\n\n")
        return
      elif choices == "강화하기":
        if self.money < 1000 * self.att_tool_Lev:
          print("돈이 부족합니다\n\n")
        elif num <= self.att_tool_Lev:
          self.money -= 1000 * self.att_tool_Lev
          self.att_tool_Lev = 1
          print("장비가 파괴되었습니다\n(그러니까 적당히 강화하라니까?)\n\n")
        elif num <= self.att_tool_Lev *plus:
          self.money -= 1000 * self.att_tool_Lev
          print("강화에 실패하셨습니다\n\n")
        else:  # 성공
          self.att_tool_Lev += 1
          self.money -= 1000 * self.att_tool_Lev
          print("강화에 성공하셨습니다\n\n")

  def sell(self):
    while True:
      choices = qu.select(
          "구매할 아이템을 선택해주세요",
          choices=["무기", "방어구", "포션", "나가기"],
      ).ask()
      if choices == "무기":
        qu.select(
            "구매할 아이템을 선택해주세요",
            choices=["마법지팡이", "검", "창", "나가기"],
        ).ask()
      elif choices == "방어구":
        qu.select(
            "구매할 아이템을 선택해주세요",
            choices=["방패", "갑옷", "투구", "나가기"],
        ).ask()
        print("방어구 메뉴입니다")
      elif choices == "포션":
        print("포션을 판매합니다")
        choices = qu.select(
            "구매하실 아이템을 선택해주세요",
            choices=[
                "공격포션",
                "엄청난 공격포션",
                "회복포션",
                "엄청난 회복포션",
                "나가기",
            ]
        ).ask()
        if choices == "공격포션":
          choice = qu.select("구매하실 개수를 선택해주세요", choices=[1, 2, 3, 4, 5]).ask()
          alpha = int(choice)
          total_price = alpha * self.potion_list[0].price
          confirm = qu.select(
              f"총 {alpha}개를 {total_price}원에 구매하시겠습니까?",
              choices=["예", "아니요"],
          ).ask()
          if confirm == "예":
            if total_price <= self.money:
              print(f"공격포션 {alpha}개를 구매하셨습니다")
              self.money -= total_price
            else:
              print("잔액이 부족합니다!")
      elif choices == "나가기":
        print("판매를 종료합니다")
        break

  def shop1(self):
    while True:
      choices = qu.select(
          "상점에 오신 것을 환영합니다\n무엇을 하시겠습니까?",
          choices=["강화하기", "구매하기", "판매하기", "나가기"],
      ).ask()
      if choices == "강화하기":
        self.rainforce()
      elif choices == "구매하기":
        print("구매하기를 선택하셨습니다\n")
        self.sell()
      elif choices == "판매하기":
        print("판매하기를 선택하셨습니다\n")
      elif choices == "나가기":
        print("상점을 나갑니다")
        break


if __name__ == "__main__":
  a = shop("검", 1, 100000000, "일반")
  a.shop1()
