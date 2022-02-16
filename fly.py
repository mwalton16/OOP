import OOP.InsectClass as ic
fly = ic.Insect()
def main():
    fly.flight_f()
    fly.get_flight()
    print("The fly has a flight distance of: "+str(fly.get_flight()))
main()