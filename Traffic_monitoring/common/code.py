class CommonResponse():
    def __init__(self):
        self.status = 200
        self.data = None

    @property
    def get(self):
        return self.__dict__