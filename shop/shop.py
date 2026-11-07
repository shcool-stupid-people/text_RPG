import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent)) # main.py기준으로 import하는 것이 호환되도록

import random
import questionary as qu
import shop.shop_manager as shop_manager
import copy

class shop:
  def __init__(self, player):
    self.shop_manager = shop_manager.shop_manager()
    self.player = player

  def rainforce(self):
    while True:
      temp = [
                qu.Choice(
                    title=f"{item.name} (가격: {item.tear}원)",
                    value=item
                )
                for item in self.player.open_inventory()
              ]
      temp.append("나가기")
      selected = qu.select(
                    "강화할 아이템을 선택해주세요",
                  choices=temp
                ).ask()
      
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
                print("장비가 파괴되었습닠다ㅋ\n\n")
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
        item_list = self.shop_manager.get_weapon_list()
        weapons = self.selling_list(item_list)
        
        buy_item = qu.select(
            "구매할 아이템을 선택해주세요",
            choices=weapons,
        ).ask()
        self.is_able_sell(buy_item)

      elif choices == "방어구":
        item_list = self.shop_manager.get_armor_list()
        armors = self.selling_list(item_list)
        
        buy_item = qu.select(
            "구매할 아이템을 선택해주세요",
            choices=armors,
        ).ask()
        self.is_able_sell(buy_item)
        
        

      elif choices == "포션":
        print("포션을 판매합니다")
        item_list = self.shop_manager.get_potion_list()
        potions = self.selling_list(item_list)

        choices = qu.select(
            "구매하실 아이템을 선택해주세요",
            choices=potions
        ).ask()

        if choices == "나가기":
                print("판매를 종료합니다")
                break
        
        choice = qu.select("구매하실 개수를 선택해주세요", choices=["1", "2", "3", "4", "5"]).ask()
        alpha = int(choice)
        total_price = alpha * choices.price
        confirm = qu.select(
            f"총 {alpha}개를 {total_price}원에 구매하시겠습니까?",
            choices=["예", "아니요"],
        ).ask()
        
        if confirm == "예":
          if total_price <= self.player.get_coin():
            print(f"{choices.name} {alpha}개를 구매하셨습니다")
            # self.money -= total_price
            self.player.change_coin(-total_price)
            self.player.add_inventory(choices, alpha)
          else:
            print("잔액이 부족합니다!")
      elif choices == "나가기":
        break

  def selling_list(self, item_list):
    temp = [
                qu.Choice(
                    title=f"{item.name} (가격: {item.price}원)",
                    value=item
                )
                for item in item_list
              ]
    temp.append("나가기")
    return temp

  def is_able_sell(self, for_buy):
    if (for_buy.price > self.player.get_coin()):
      print("금액이 부족합니다")
    else:
      self.player.change_coin(-for_buy.price)
      for_buy = copy.deepcopy(for_buy)
      self.player.add_inventory(for_buy)

  def buy(self):
    temp = [
              qu.Choice(
                  title=f"{item.name} (가격: {item.price}원)",
                  value=item
              )
              for item in self.player.open_inventory()
            ]
    temp.append("나가기")
    selected = qu.select(
                  "판매할 아이템을 선택해주세요",
                choices=temp
              ).ask()
    if (selected == "나가기"):
      pass

    else:
      self.player.change_coin(selected.price)
      self.player.del_inventory(selected)
  
  def start_shop(self):
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
        self.buy()

      elif choices == "나가기":
        print("상점을 나갑니다")
        break


