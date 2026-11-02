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

#generate managers
skill_manager = sk.skill_manager()

#generate player
a = player.player(skill_manager)

world = map.field(a)
world.generate_room()

while(1):
    check_grid = world.check_grid()

    move = questionary.select(
        message="이동 선택하세요",
        choices=check_grid
    ).ask()

    if (move == "exit"):
        break