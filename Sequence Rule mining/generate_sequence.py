f2 = open("unique_customer_id.txt","r")
f3 = open("item_id_description_mapping.csv","r")
f4 = open("item_id_number_mapping.txt","r")
f5 = open("sequence_data.txt","w")
from datetime import datetime,date
item_number = {}
for line in f4.readlines():
    j = line.split(",")
    item_number[j[1][:-1]] = j[0]
cust_id = []
for line in f2.readlines():
    cust_id.append(line[:-1])
#l = f1.readline()
seq=[]
m_date = datetime.strptime("12/1/10","%m/%d/%y")
#cust_id=[17850]
for cust in cust_id:
    cust_lines = []
    cust_seq=[]
    temp_seq=[]
    for i in range(51):
        temp_seq.append([])
    
    f1 = open("online_retail.csv","r")
    for line in f1.readlines():
        j = line.split(",")
        #print(cust,j[-2])
        if str(cust) == str(j[-2]):
            k = datetime.strptime(j[-4].split()[0],"%m/%d/%y")
            days = (k-m_date).days
            temp_seq[days].append(int(item_number[j[1]]))
    seq.append(temp_seq)
    f1.close()
#print(seq)
for cust in seq:
    for day in cust:
        day.sort()
        if len(day) == 0:
            f5.write("-1 ")
        else:
            for i in day:
                f5.write(str(i))
                f5.write(" ")
            f5.write("-1 ")
    f5.write("-2\n")

            
#     print(cust_lines)
#     for line in cust_lines:
#         print(temp_date)
#         j = line.split(",")
#         if str(temp_date) == str(j[-4].split()[0]):
#             temp_seq.append(item_number[j[1]])
#         else:
#             temp_seq.sort()
#             cust_seq.append(temp_seq)
#             temp_seq=[]
#             d = j[-4].split()[0]
#             #print(d)
#             d1 = datetime.strptime(d,'%m/%d/%y')
#             #print(d1)
#             d2 = datetime.strptime(temp_date,'%m/%d/%y')
#             days = (d1-d2).days
#             for day in range(days-1):
#                 cust_seq.append([])
#             temp_date = j[-4].split()[0]
#             temp_seq.append(item_number[j[1]])
#     seq.append(cust_seq)
#     f1.close()
#     break
# print(seq)