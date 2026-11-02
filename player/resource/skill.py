class skill():
    def __init__(self, name, cost, mp, rank):
        self.name = name
        self.cost = cost
        self.mp = mp
        self.rank = rank

    def get_name(self):
        return self.name
    
    def get_cost(self):
        return self.cost

    def get_mp(self):
        return self.mp

    def get_rank(self):
        return self.rank