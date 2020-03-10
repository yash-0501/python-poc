def person(name, **data):
    print(name)
    print(data)

    for i,j in data.items(): #iterate different items in dict
        print(i,"-",j)

person('Yash',age=20,city='Agra',pin=282007) #keyword args

#dictionary - kwargs