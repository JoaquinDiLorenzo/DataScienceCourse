#1
word_stats={}

with open("poem.txt","r") as file:
    text=file.read()

words = text.split()

for word in words:
    if word in word_stats:
        word_stats[word.lower()]+=1
    else:
        word_stats[word.lower()]=1

max_word = max(word_stats.items(), key=lambda x: x[1])

#print(max_word)


#2
import csv

with open('stocks.csv',"r") as input, \
    open("output.csv","w",newline='') as output:

    reader_csv = csv.DictReader(input)
    
    headers=['Company Name', 'PE Ratio', 'PB Ratio']

    writer_csv = csv.DictWriter(output, fieldnames=headers)

    data = []

    for line in reader_csv:
        try:
            PE=float(line['Price']) / float(line['Earnings Per Share'])
            PB=float(line['Price']) / float(line['Book Value'])
            data.append({'Company Name': line['Company Name'], 'PE Ratio':round(PE,2),'PB Ratio':round(PB,2)})
        except ValueError as e:
            print(f"Error en la linea : {line}. Error: {e}")
            continue
        
    writer_csv.writeheader()
    writer_csv.writerows(data)