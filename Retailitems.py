import RetailitemClass as r

def main_1():
    item_1 = r.Retailitem
    item_1.descript(item_1,"Jacket")
    item_1.units(item_1,"12")
    item_1.price(item_1,"$59.95")
    print("Item: 1"+"\n"+"Description: "+item_1.description+"\n"+"Units: "+item_1.unit+"\n"+"Price: "+item_1.price_per_unit)
main_1()

def main_2():
    item_2 = r.Retailitem
    item_2.descript(item_2,"Designer Jeans")
    item_2.units(item_2,"40")
    item_2.price(item_2,"$34.95")
    print("Item: 2"+"\n"+"Description: "+item_2.description+"\n"+"Units: "+item_2.unit+"\n"+"Price: "+item_2.price_per_unit)
main_2()

def main_3():
    item_3 = r.Retailitem
    item_3.descript(item_3,"Shirt")
    item_3.units(item_3,"20")
    item_3.price(item_3,"$24.95")
    print("Item: 3"+"\n"+"Description: "+item_3.description+"\n"+"Units: "+item_3.unit+"\n"+"Price: "+item_3.price_per_unit)
main_3()
