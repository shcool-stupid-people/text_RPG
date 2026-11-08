class skill():
    def __init__(self, *, name, cost, mp, rank, skill_type="attack", damage=0):
        self.name = name
        self.cost = cost
        self.mp = mp
        self.rank = rank
        self.skill_type = skill_type
        self.damage = damage

    def __str__(self):
        return f"스킬 이름: {self.name}, 스킬 타입: {self.skill_type}, \
            스킬 등급: {self.rank}, 스킬 MP 소모량: {self.mp}, 스킬 데미지: {self.damage}\n"

    def __repr__(self):
        return f"스킬 이름: {self.name}, 스킬 타입: {self.skill_type}, \
            스킬 등급: {self.rank}, 스킬 MP 소모량: {self.mp}, 스킬 데미지: {self.damage}\n"
    
    def get_name(self):
        return self.name
    
    def get_cost(self):
        return self.cost

    def get_mp(self):
        return self.mp

    def get_rank(self):
        return self.rank

    def get_skill_type(self):
        return self.skill_type
    
    def get_damage(self):
        return self.damage

class Attack_skill(skill):
    def __init__(self, *, name, cost, mp, rank, damage):
        super().__init__(name=name, cost=cost, mp=mp, rank=rank, skill_type="attack", damage=damage)

class Effect_skill(skill):
    def __init__(self, *, name, cost, mp, rank):
        super().__init__(name=name, cost=cost, mp=mp, rank=rank, skill_type="effect", damage=0)

    def use_effect_skill(self, target):
        '''스킬의 효과를 지정해 두는 거'''
        print("나는 똥이다")

class Cure_effect_skill(Effect_skill):
    def __init__(self, *, name, cost, mp, rank):
        super().__init__(name=name, cost=cost, mp=mp, rank=rank)

    def use_effect_skill(self, target):
        print(f"{target.get_name()}의 체력을 35 회복했습니다.")
        target.change_hp(35)
