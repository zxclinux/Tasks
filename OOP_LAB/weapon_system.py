class WeaponSystem:
    def __init__(self, weapon_type="NoWeapon"):
        self.weapon_type = weapon_type

    def weapon_info(self):
        return f"Weapon system: {self.weapon_type}"
