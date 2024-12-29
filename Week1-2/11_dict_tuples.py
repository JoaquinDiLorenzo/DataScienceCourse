#1
dict={'China':142, 'India':136,'USA':32,'Pakistan':21}

def print_all():
    for c in dict:
        print(c,"==>",dict[c])

def add():
    name=input("Enter a country name: ")
    if name not in dict:
        pop=input("Enter the population: ")
        dict[name]=pop
        print_all()
    else:
        print("That country already exist.")

def remove():
    name=input("Enter a country to remove: ")
    if name in dict:
        del dict[name]
        print_all()
    else:
        print("That country doesnt exist")

def query():
    name=input("Enter a country: ")
    if name in dict:
        print(name, "==>", dict[name])
    else:
        print("That country doesnt exist")

def main1():
    finish=False
    while not finish:
        op=int(input("Enter operation (1.add, 2.remove, 3.query, 4.print, 5.exit):"))
        if op == 1:
            add()
        elif op == 2:
            remove()
        elif op == 3:
            query()
        elif op == 4:
            print_all()
        else:
            finish=True

#main1()

#2
import statistics
stocks={'info':[600,630,620], 'ril':[1430,1490,1567], 'mtl':[234,180,160]}

def print_stocks():
    for key,value in stocks.items():
        avg=statistics.mean(value)
        print(key,"==>", value, "==> avg: ", round(avg,2))

def add_stock():
    name=input("Enter the name of the stock: ")
    price=int(input("Enter the price of the stock: "))
    if name in stocks:
        stocks[name].append(price)
    else:
        stocks[name] = price

def main2():
    finish=False
    while not finish:
        op=int(input("1.print, 2.add"))
        if op==1:
            print_stocks()
        elif op==2:
            add_stock()
        else:
            finish=True

main2()