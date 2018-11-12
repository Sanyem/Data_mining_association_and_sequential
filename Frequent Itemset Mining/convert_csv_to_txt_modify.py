f1 = open("transactions_item_id.csv","r")
f2 = open("transactions_item_id.txt","w")
f3 = open("item_id_description_mapping.csv","r")
i = 1
dic = {}
for line in f3.readlines():
    j = line.split(",")
    dic[j[0]] = i
    i = i+ 1
for line in  f1.readlines():
    j = line.split(",")
    for i in j:
        f2.write(i)
        f2.write(" ")
    f2.write('\n')

