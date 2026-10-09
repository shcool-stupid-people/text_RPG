import random


class enemy:

    def __init__(self, name, skill, hp):
        self.probability_list = []
        self.enemy_name = name
        self.skill_list = skill  # enemy_manager에서 전달받은 스킬 리스트
        self.hp = hp
        self.max_hp = hp
        self.enemy_action_percent()

    def enemy_action_percent(self):
        """스킬 개수에 따라 앞쪽 스킬에 더 높은 확률을 부여하는 확률 리스트 생성"""
        self.probability_list = []
        temp = len(self.skill_list)

        if temp == 0:
            return

        # 변수명 중복 해결 (i -> idx, j)
        # 예: 스킬이 3개일 때 -> 인덱스 0은 3번, 인덱스 1은 2번, 인덱스 2는 1번 추가
        for idx in range(temp):
            weight = temp - idx
            for _ in range(weight):
                self.probability_list.append(idx)

    def use_skill(self):
        """확률 리스트에서 스킬 하나를 무작위로 뽑아 사용"""
        if not self.skill_list:
            # 스킬이 없을 경우 기본 공격 예외 처리
            print(f"{self.enemy_name}의 기본 공격!")
            return {"name": "기본 공격", "damage": 5}

        select_idx = random.choice(self.probability_list)
        selected_skill = self.skill_list[select_idx]

        # selected_skill 구조 예시: {'name': 'attack', 'damage': 10}
        skill_name = selected_skill.get("name", "스킬")
        print(f"{self.enemy_name}이(가) [{skill_name}] 스킬을 사용했습니다!")

        return selected_skill

    def take_damage(self, damage):
        """플레이어로부터 데미지를 입을 때 사용"""
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(
            f"{self.enemy_name}이(가) {damage}의 피해를 입었습니다. (남은 HP: {self.hp}/{self.max_hp})"
        )

    def is_alive(self):
        """적 생존 여부 확인"""
        return self.hp > 0

    def set_hp(self, hp):
        self.hp += hp

    def get_hp(self):
        return self.hp

    def get_name(self):
        return self.enemy_name