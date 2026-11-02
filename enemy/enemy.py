import random

import entity

class enemy(entity.Monster):
    def __init__(self,name, skill, hp, gold, drops):
        self.probability_list = []
        self.name = name
        self.skill_list = skill
        self.max_hp = hp
        self.hp = hp
        super().__init__(hp)

        self.gold = gold
        self.drops = [] if drops is None else drops
        self.enemy_action_percent()

    def enemy_action_percent(self):
        """스킬 개수에 따라 앞쪽 스킬에 더 높은 확률을 부여하는 확률 리스트 생성"""
        self.probability_list = []
        count = len(self.skill_list)

        if count == 0:
            return

        # 변수명 중복 해결 (i -> idx, j)
        # 예: 스킬이 3개일 때 -> 인덱스 0은 3번, 인덱스 1은 2번, 인덱스 2는 1번 추가
        for idx in range(count):
            weight = count - idx
            for _ in range(weight):
                self.probability_list.append(idx)

    def use_skill(self):
        """확률 리스트에서 스킬 하나를 무작위로 뽑아 사용"""
        if not self.skill_list:
            # 스킬이 없을 경우 기본 공격 예외 처리
            print(f"{self.name}의 기본 공격!")
            return {"name": "기본 공격", "damage": 5}

        select_idx = random.choice(self.probability_list)
        selected_skill = self.skill_list[select_idx]

        return selected_skill

    def attack(self, target):
        skill = self.use_skill()
        damage = skill.get("damage", self.attack_power)

        print(f"{self.name}이(는) [{skill.get('name', '스킬')}]을(를) 사용했다.")
        target.on_hit(damage)

        debuff = skill.get("debuff")
        if debuff and target.hp > 0:
            self.apply_debuff(target, debuff)

        print(f"{self.name}의 체력: {self.hp}, {target.name}의 체력: {target.hp}\n")

    def apply_debuff(self, target, debuff):
        if hasattr(target, "add_debuff"):
            target.add_debuff(debuff)
        else:
            print(f"[sys]: {target.name}에게 디버프 {debuff['type']} (아직 처리 코드 없음)")

    def take_damage(self, damage):
        """플레이어로부터 데미지를 입을 때 사용"""
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(
            f"{self.name}이(가) {damage}의 피해를 입었습니다. (남은 HP: {self.hp}/{self.max_hp})"
        )

    def is_alive(self):
        """적 생존 여부 확인"""
        return self.hp > 0

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def change_hp(self, hp):
        """player.change_hp와 같은 이름 규칙 (값을 더함)"""
        self.hp += hp

    def get_gold(self):
        return self.gold

    def roll_drops(self):
        """처치 시 호출. 확률(%)에 따라 얻은 부산물 이름 리스트 반환"""
        return [d["name"] for d in self.drops if random.randint(1, 100) <= d["chance"]]
