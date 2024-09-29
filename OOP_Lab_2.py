def log_method_call(func):
    def wrapper(*args, **kwargs):
        print(f"Method called: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class Airplane:

    airplane_count = 0

    def __init__(self, brand="NoBrand", model="NoModel", max_speed=0, max_altitude=0):
        self._brand = brand  
        self._model = model  
        self.max_speed = max_speed
        self.max_altitude = max_altitude
        Airplane.airplane_count += 1

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @log_method_call
    def cost(self):
        return self.max_speed * 1000 + self.max_altitude * 100

    def __str__(self):
        return f"{self.brand} {self.model}: Max Speed {self.max_speed} km/h, Max Altitude {self.max_altitude}"

    @staticmethod
    def airplane_info():
        return f"Total number of airplanes: {Airplane.airplane_count}"

class FighterJet(Airplane):

    @log_method_call
    def cost(self):
        return super().cost() * 2

class WeaponSystem:
    def __init__(self, weapon_type="NoWeapon"):
        self.weapon_type = weapon_type

    def weapon_info(self):
        return f"Weapon system: {self.weapon_type}"

class CombatFighter(FighterJet, WeaponSystem):
    def __init__(self, brand, model, max_speed, max_altitude, weapon_type):
        FighterJet.__init__(self, brand, model, max_speed, max_altitude)
        WeaponSystem.__init__(self, weapon_type)

    def __str__(self):
        return f"{self.brand} {self.model} with {self.weapon_type}: Speed {self.max_speed} km/h, Altitude {self.max_altitude}"
    
    @log_method_call
    def cost(self):
        return super().cost() * 3
    
#-------------------------------------------------------------------------------------------------------------------------------

airplane = Airplane("Boeing", "747", 900, 12000)
print(airplane)
print(f"Airplane cost: {airplane.cost()}")

fighter_jet = FighterJet("Lockheed", "F-22", 1500, 20000)
print(fighter_jet)
print(f"Fighter jet cost: {fighter_jet.cost()}")

combat_fighter = CombatFighter("Sukhoi", "Su-35", 1800, 22000, "Missiles")
print(combat_fighter)
print(f"Combat fighter cost: {combat_fighter.cost()}")
print(combat_fighter.weapon_info())

print(Airplane.airplane_info())