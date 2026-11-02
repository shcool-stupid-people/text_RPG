from .skill import skill
import os
import json

class skill_manager():
    def __init__(self):
        self.skills = []
        self.init_skills()
        

    def init_skills(self):
        for root, dirs, files in os.walk("player\\resource"):
            for file_name in files:
                if not file_name.endswith(".json"):
                    continue

                file_path = os.path.join(root, file_name)

                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                for _ in range(len(data)):
                    self.skills.append(skill(data[_]["name"], data[_]["cost"], data[_]["mp"], data[_]["rank"]))

                
