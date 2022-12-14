
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
|  Total Faction Health : {} | 
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
        
        
class Orcs(Faction):
    def __init__(self,name):
        super().__init__(name) 
    
    def PerformAttack(self):
        #first_enemy : Dwarwes , second_enemy : Elves
        #Tek düşman varsa saldırı puanı olan tüm birimlerle saldır.
        if (self.first_enemy.is_alive and not self.second_enemy.is_alive): 
            self.first_enemy.ReceiveAttack(super().PerformAttack(), 'Orcs')
        
        elif (not self.first_enemy.is_alive and self.second_enemy.is_alive):
            self.second_enemy.ReceiveAttack(super().PerformAttack(), 'Orcs')
        #İkisi de hayattaysa %70 i elflerle geri kalanlar cücelere.
        elif (self.first_enemy.is_alive and self.second_enemy.is_alive):
            self.first_enemy.ReceiveAttack(super().PerformAttack()*0.3, 'Orcs')
            self.second_enemy.ReceiveAttack(super().PerformAttack()*0.7, 'Orcs')


    def ReceiveAttack(self, damage, obj):
        if obj == 'Elves':
            super().ReceiveAttack(0.75*(damage/self.health_point))
        elif obj == 'Dwarves':
            super().ReceiveAttack(0.8*(damage/self.health_point))

            
    def PurchaseWeapons(self, weapon_bought):
        return (super().PurchaseWeapons(2*weapon_bought, 20*weapon_bought))
    
    def PurchaseArmors(self, armor_bought):
        return (super().PurchaseArmors(3*armor_bought, 1*armor_bought))
    
    def Print(self):
        print("Stop running, you'll only die tired!")
        super().Print()
        
        
class Dwarves(Faction):
    def __init__(self,name):
        super().__init__(name) 
        
    
    def PerformAttack(self):
        #first_enemy : Orcs , second_enemy : Elves
        
        if (self.first_enemy.is_alive and not self.second_enemy.is_alive):
            self.first_enemy.ReceiveAttack(super().PerformAttack(), 'Dwarves')
        
        elif (not self.first_enemy.is_alive and self.second_enemy.is_alive):
            self.second_enemy.ReceiveAttack(super().PerformAttack(), 'Dwarves')
            
        elif (self.first_enemy.is_alive and self.second_enemy.is_alive):
            self.first_enemy.ReceiveAttack(super().PerformAttack()/2, 'Dwarves')
            self.second_enemy.ReceiveAttack(super().PerformAttack()/2, 'Dwarves')

    
    def ReceiveAttack(self, damage, obj):
        super().ReceiveAttack(damage/self.health_point)
        

    def PurchaseWeapons(self, weapon_bought):
        return (super().PurchaseWeapons(weapon_bought, 10*weapon_bought))
    
    
    def PurchaseArmors(self, armor_bought):
        return (super().PurchaseArmors(2*armor_bought, 3*armor_bought))
    
    
    def Print(self):
        print("Taste the power of our axes!")
        super().Print()
        
        
class Elves(Faction):
    def __init__(self, name = "just elves"):
        super().__init__(name) 
        
    def PerformAttack(self): 
        #first_enemy : Orcs , second_enemy : Dwarwes
        
        if (self.first_enemy.is_alive and not self.second_enemy.is_alive):
            self.first_enemy.ReceiveAttack(super().PerformAttack(), 'Elves')
        
        elif (not self.first_enemy.is_alive and self.second_enemy.is_alive):
            self.second_enemy.ReceiveAttack(super().PerformAttack()*1.5, 'Elves')
            
        elif (self.first_enemy.is_alive and self.second_enemy.is_alive):
            self.first_enemy.ReceiveAttack(super().PerformAttack()*0.6, 'Elves')
            self.second_enemy.ReceiveAttack(super().PerformAttack()*0.4*1.5, 'Elves')

            
    def ReceiveAttack(self, damage, obj):
        if obj == 'Orcs':
            super().ReceiveAttack(damage/self.health*1.25)
        
        elif obj == 'Dwarves':
            super().ReceiveAttack(damage/self.health_point*0.75)


    def PurchaseWeapons(self, weapon_bought):
        return(super().PurchaseWeapons(2*weapon_bought, 15*weapon_bought))
        
    def PurchaseArmors(self, armor_bought):
        return(super().PurchaseArmors(4*armor_bought, 5*armor_bought))
        
    def Print(self):
        print("You cannot reach our elegance.")
        super().Print()        
        
        
class Merchant:
    def __init__(self, start_weapon=10, start_armor=10):
        self.start_weapon = start_weapon
        self.start_armor = start_armor
        self.EndTurn()
        self.revenue = 0
        
    def AssgnFaction(self, f, s, t):
        # first_faction : Orcs second_faction : Dwarwes third_faction : Elves
        self.first_faction = f 
        self.second_faction = s 
        self.third_faction = t 
        
    def SellWeapons(self, to_whom, weapons_to_sell):
        if to_whom == 'Orcs': 
            to_whom = self.first_faction
        elif to_whom == 'Dwarves': 
            to_whom = self.second_faction
        elif to_whom == 'Elves':
            to_whom = self.third_faction

        if not to_whom.is_alive: print("The faction you want to sell weapons is dead!")
        else:
            if weapons_to_sell > self.weapon_num: 
                print("You try to sell more weapons than you have in possession")
                return False
            
            else:
                self.revenue += to_whom.PurchaseWeapons(weapons_to_sell)
                print("Weapons sold!")
                self.weapon_num -= weapons_to_sell
                return True
        
        
    def SellArmors(self, to_whom, armors_to_sell):
        if to_whom == 'Orcs': 
            to_whom = self.first_faction
        elif to_whom == 'Dwarves':
            to_whom = self.second_faction
        elif to_whom == 'Elves':
            to_whom = self.third_faction

        
        if not to_whom.is_alive: print("The faction you want to sell armors is dead!")
        else:
            if armors_to_sell > self.armor_num: 
                print("You try to sell more armors than you have in possession")
                return False
            
            else:
                self.revenue += to_whom.PurchaseArmors(armors_to_sell)
                print("Armors sold!")
                self.armor_num -= armors_to_sell
                return True
            
    
    def EndTurn(self): 
        self.weapon_num = self.start_weapon
        self.armor_num = self.start_armor
        
        
        
        
        
        
        
        
        
        
        
        
        
        