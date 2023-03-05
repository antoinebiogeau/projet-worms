import random

class Wind:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.wind = (0, 0)
        return cls.instance

    def getWind(self):
        return self.wind

    def update(self):
        self.wind = (random.randint(-5, 5), random.randint(-5, 5))
        print(f"{self.wind[0]}:{self.wind[1]}")