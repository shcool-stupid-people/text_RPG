from .skill import *
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
                    if skill_data["type"] == "attack":
                        self.skills.append(Attack_skill(name=skill_data["name"], cost=skill_data["cost"], 
                                             mp=skill_data["mp"], rank=skill_data["rank"], damage=skill_data["damage"]))
                    elif skill_data["type"] == "effect":
                        if skill_data["subtype"] == "cure":
                            self.skills.append(Cure_effect_skill(name=skill_data["name"], cost=skill_data["cost"], 
                                             mp=skill_data["mp"], rank=skill_data["rank"]))
                        else:
                            self.skills.append(Effect_skill(name=skill_data["name"], cost=skill_data["cost"], 
                                             mp=skill_data["mp"], rank=skill_data["rank"]))
