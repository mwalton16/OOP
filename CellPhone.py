import CellPhoneClass as c

nokia = c.Cellphone("Nokia","3310",200)
def main():
    print("The Manufacturer is: ",nokia.get_manufact())
    print("The Model is: ",nokia.get_model())
    print("The Price is: ",nokia.get_retail_price())
main()