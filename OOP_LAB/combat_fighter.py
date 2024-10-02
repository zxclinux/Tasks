from fighter_jet import FighterJet
from weapon_system import WeaponSystem
from log_decorator import log_method_call

class CombatFighter(FighterJet, WeaponSystem):
    def __init__(self, brand, model, max_speed, max_altitude, weapon_type):
        FighterJet.__init__(self, brand, model, max_speed, max_altitude)
        WeaponSystem.__init__(self, weapon_type)

    def __str__(self):
        return f"{self.brand} {self.model} with {self.weapon_type}: Speed {self.max_speed} km/h, Altitude {self.max_altitude}"
    
    @log_method_call
    def cost(self):
        return super().cost() * 3
