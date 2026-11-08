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

                for i in range(len(data)):
                    skill_data = data[i]
                    self.skills.append(skill(skill_data["name"], skill_data["cost"], 
                                             skill_data["mp"], skill_data["rank"]))

                
