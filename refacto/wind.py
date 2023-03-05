class Wind:
    instance = None

    def __init__(self):
        self.wind = (0,0)

    def __call__(self, *args, **kwds):
        if self.instance is None:
            self.instance = super().__new__(self)
        return self.instance

    def getWind(self):
        return self.wind()

    def update(self):
        print("Updating wind")