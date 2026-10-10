import random

import entity


class enemy(entity.Monster):
    """entity.Monster를 상속한 적 클래스.

    Being의 attack / on_hit / on_death / is_death를 그대로 쓰고,
    attack만 스킬 방식으로 덮어쓴다. (MonsterBattler가 obj.attack(target.obj)를 호출함)
    """

    def __init__(self, name, skill, hp, gold=0, drops=None):
        # Being.__init__이 max_hp 범위를 검사하므로 먼저 설정
        self.name = name
        self.max_hp = hp
        super().__init__(hp)

        self.skill_list = skill  # [{"name":..., "damage":..., "debuff":{...}}, ...]
        self.gold = gold
        self.drops = drops or []  # [{"name":..., "chance":...}, ...]
        self.probability_list = []
        self.enemy_action_percent()

    def enemy_action_percent(self):
        """앞쪽 스킬일수록 높은 확률을 갖는 확률 리스트 생성
        예: 스킬 3개 -> 인덱스 0은 3번, 1은 2번, 2는 1번 추가"""
        self.probability_list = []
        count = len(self.skill_list)

        for idx in range(count):
            for _ in range(count - idx):
                self.probability_list.append(idx)

    def use_skill(self):
        """확률 리스트에서 스킬 하나를 뽑아 반환 (스킬이 없으면 기본 공격)"""
        if not self.skill_list:
            return {"name": "기본 공격", "damage": self.attack_power}

        return self.skill_list[random.choice(self.probability_list)]

    def attack(self, target):
        """Being.attack을 스킬 방식으로 덮어쓰기"""
        skill = self.use_skill()
        damage = skill.get("damage", self.attack_power)

        print(f"{self.name}이(는) [{skill.get('name', '스킬')}]을(를) 사용했다.")
        target.on_hit(damage)

        debuff = skill.get("debuff")
        if debuff and target.hp > 0:
            self.apply_debuff(target, debuff)

        print(f"{self.name}의 체력: {self.hp}, {target.name}의 체력: {target.hp}\n")

    def apply_debuff(self, target, debuff):
        """디버프를 대상에게 전달.
        debuff = {"type": "poison|weaken|dehydration", "value": n, "turns": n}
        대상이 add_debuff(debuff)를 구현하면 그쪽에서 처리하고, 없으면 안내만 출력"""
        if hasattr(target, "add_debuff"):
            target.add_debuff(debuff)
        else:
            print(f"[sys]: {target.name}에게 디버프 {debuff['type']} (아직 처리 코드 없음)")

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
