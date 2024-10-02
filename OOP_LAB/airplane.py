from log_decorator import log_method_call

class Airplane:

    MAX_SPEED_COST = 1000
    MAX_ALTITUDE_COST = 100

    airplane_count = 0

    def __init__(self, brand="NoBrand", model="NoModel", max_speed=0, max_altitude=0):
        self._brand = brand  
        self._model = model  
        self.max_speed = max_speed
        self.max_altitude = max_altitude
        self.increment_airplane_count()

    @classmethod
    def increment_airplane_count(cls):
        cls.airplane_count += 1

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
        return self.max_speed * self.MAX_SPEED_COST + self.max_altitude * self.MAX_ALTITUDE_COST

    def __str__(self):
        return f"{self.brand} {self.model}: Max Speed {self.max_speed} km/h, Max Altitude {self.max_altitude}"

    @staticmethod
    def airplane_info():
        return f"Total number of airplanes: {Airplane.airplane_count}"
