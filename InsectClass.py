import random

class Insect:
    def __init__(self):
        self.wings = "2"
        self.legs = "4"
        self.flight = "0"
    def flight_f(self):
        self.flight = str(random.randint(1,10))
    def get_flight(self):
        print(self.flight)
       

