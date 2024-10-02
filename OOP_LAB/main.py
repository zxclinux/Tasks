from airplane import Airplane
from fighter_jet import FighterJet
from combat_fighter import CombatFighter

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
