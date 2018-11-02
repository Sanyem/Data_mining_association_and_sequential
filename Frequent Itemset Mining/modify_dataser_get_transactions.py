import csv
f1 = open("online_retail.csv","r")
f2 = open("transactions_item_id.csv","w")
f3 = open("item_id_description_mapping.csv","w")
f1.readline()
invoice_no = 1
transactions = []
map_set = set()
arr=[]
for line in f1.readlines():
    line_arr = line.split(',')
    if invoice_no == line_arr[0]:
        arr.append(line_arr[1])
    elif invoice_no != line_arr[0]:
        invoice_no = line_arr[0]
        transactions.append(arr)
        arr=[]
        arr.append(line_arr[1])
    map_set.add(tuple([line_arr[1],line_arr[2]]))
    print(line)
writer = csv.writer(f2, delimiter=',')
#print(transactions[1])
for j in transactions:
    writer.writerow(j)
w = csv.writer(f3,delimiter=',')
for j in map_set:
    w.writerow(j)