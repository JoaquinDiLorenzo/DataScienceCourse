#1
list=[2200,2350,2600,2130,2190]

#1_1
feb_extra=list[1]-list[0]
print(feb_extra)

#1_2
first_quarter=0
for i in range(3):
    first_quarter+=list[i]
print(first_quarter)

#1_3
print(2000 in list)

#1_4
list.append(1900)
print(list)

#1_5
list[3]=list[3]-200
print(list)

#2
heros=['spider man','thor','hulk','iron man','captain america']

#2_1
print(len(heros))

#2_2
heros.append("black panther")
print(heros)

#2_3
heros.remove("black panther")
heros.insert(3,"black panther")
print(heros)

#2_4
heros[1:3]=["doctor Strange"]
print(heros)
