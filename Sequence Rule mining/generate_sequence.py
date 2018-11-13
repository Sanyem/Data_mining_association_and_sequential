f1 = open("online_retail.csv","r")
f2 = open("unique_customer_id.txt","r")
f3 = open("item_id_description_mapping.csv","r")
f4 = open("item_id_number_mapping.txt","r")
from datetime import datetime,date
item_number = {}
for line in f4.readlines():
    j = line.split(",")
    item_number[j[1][:-1]] = j[0]
cust_id = []
for line in f2.readlines():
    cust_id.append(line[:-1])
l = f1.readline()
seq=[]
for cust in cust_id:
    cust_lines = []
    for line in f1.readlines():
        j = line.split(",")
        if str(cust) == str(j[-2]):
            cust_lines.append(line)
    inv_id = ""
    temp_date = ""
    cust_seq=[]
    temp_seq=[]
    for line in cust_lines:
        j = line.split(",")
        if temp_date == j[-4].split()[0]:
            temp_seq.append(item_number[j[1]])
        else:
            temp_seq.sort()
            cust_seq.append(temp_seq)
            temp_seq=[]
            d = j[-4].split()[0]
            d1 = datetime.strptime(d,"%d/%m/%y")
            d2 = datetime.strptime(temp_date,"%d/%m/%y")
            days = (d1-d2).days
            for day in range(days):
                cust_seq.append([])
            temp_date = j[-4].split()[0]
            temp_seq.append(item_number[j[1]])
    seq.append(cust_seq)
print(seq)