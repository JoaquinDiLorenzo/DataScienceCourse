india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

#1
city = input("Enter a city: ")
if city in india:
    print(city, " is in India")
elif city in pakistan:
    print(city, " is in pakistan")
elif city in bangladesh:
    print(city, " is in bangladesh")

#2
city1 = input("Enter a city: ")
city2 = input("Enter a city: ")
if city1 in india and city2 in india:
    print("Both cities are in india")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in paklistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in bangladesh")

#3
sugar=input("Enter you sugar level: ")
if sugar < 80:
    print("Your sugar is low")
elif sugar >100:
    print("Your sugar is high")
else:
    print("Your sugar is normal")
