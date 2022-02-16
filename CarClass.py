class Car:
    def __init__(self):
        self.__year = ""
        self.__make =""
        self.__speed = 0
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5
    def get_speed(self):
        print("The car is traveling at "+str(self.__speed)+" miles per hour.")

