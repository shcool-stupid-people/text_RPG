import json
import os
import random
import enemy


class enemy_manager:
    def __init__(self):
        self.data_list = []
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.resource_file_dir = os.path.join(
            BASE_DIR, "resorce"
        )  # text_RPG/resorce
        self.load_enemy_data()

    def load_enemy_data(self):
        for root, dirs, files in os.walk(self.resource_file_dir):
            for file_name in files:
                if not file_name.endswith(".json"):
                    continue

                file_path = os.path.join(root, file_name)

                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                    floor_idx = data["floor"] - 1

                    # data_list 길이가 모자라면 빈 리스트를 채워 인덱스 에러 방지
                    while len(self.data_list) <= floor_idx:
                        self.data_list.append([])

                    self.data_list[floor_idx].append(data)

    def select_enemy(self, floor):
        if floor - 1 >= len(self.data_list) or not self.data_list[floor - 1]:
            raise ValueError(f"{floor}층에 해당하는 적 데이터가 없습니다!")

        selected_enemy = random.choice(self.data_list[floor - 1])
        return self.generate_enemy(selected_enemy)

    def parse_skills(self, raw_skills):
        parsed = []
        for item in raw_skills:
            if isinstance(item, list):
                parsed.append(dict(item))
            else:
                parsed.append(item)
        return parsed

    def generate_enemy(self, enemy_data):
        # 중첩 리스트 스킬 구조일 경우 dict 변환 후 처리
        raw_skill = enemy_data.get("skill", [])
        if raw_skill and isinstance(raw_skill[0], list):
            formatted_skills = self.parse_skills(raw_skill)
        else:
            formatted_skills = raw_skill

        temp = enemy.enemy(
            name=enemy_data["name"],
            skill=formatted_skills,
            hp=enemy_data["hp"]
        )
        return temp