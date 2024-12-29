#1
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
cant=0
for item in result:
    if item=="heads":
        cant+=1
print(cant)

#2
for i in range(1,11):
    if i%2!=0:
        print(i*i)

#4
for i in range(1,6):
    s=''
    for j in range(i):
        s+='*'
    print(s)
