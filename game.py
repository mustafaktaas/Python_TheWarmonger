
class Faction:
    def __init__(self, name="Default", unit_num = 50, attack_point = 30, health_point = 150, reg_num = 10):
        self.name = name 
        self.unit_num = unit_num 
        self.attack_point = attack_point
        self.health_point = health_point
        self.reg_num = reg_num 
        self.total_health = self.unit_num * self.health_point
        self.is_alive = True 
        
    def AssgnEnemies(self, first_enemy, second_enemy):
        self.first_enemy = first_enemy 
        self.second_enemy = second_enemy
        
    def PerformAttack(self):
        return self.unit_num * self.attack_point / 100
    
    def ReceiveAttack(self, damage):
        self.unit_num = self.unit_num - damage
        

    def PurchaseWeapons(self, increase_attack, profit):
        self.attack_point = self.attack_point + increase_attack 
        return profit
        
        
    def PurchaseArmors(self, increase_health, profit):
        self.health_point = self.health_point + increase_health 
        return profit
    
    def Print(self):
        print("""
|  Faction Name         : {} | 
|  Status               : {} | 
|  Number of Units      : {} | 
|  Attack Point         : {} | 
|  Health Point         : {} | 
|  Unit Regen Number    : {} | 
| Total Faction Health : {} | 
        """.format(self.name,
        'Alive' if self.is_alive == True else 'Defeated',
        self.unit_num,
        self.attack_point,
        self.health_point,
        self.reg_num,
        self.total_health))

    def EndTurn(self): 
        self.unit_num = self.unit_num + self.reg_num
        if self.unit_num <= 0: self.unit_num = 0; self.is_alive = False 
        self.total_health = self.unit_num * self.health_point