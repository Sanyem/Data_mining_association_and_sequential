f1 = open("transactions_item_id.csv","r")
f2 = open("transactions_item_id.txt","w")
f3 = open("item_id_description_mapping.csv","r")
f4 = open("item_id_number_mapping.txt","w")
i = 1
dic = {}
for line in f3.readlines():
    j = line.split(",")
    dic[j[0]] = i
    f4.write(str(i))
    f4.write(",")
    f4.write(j[0])
    f4.write("\n")
    i = i + 1
print(dic)
for line in  f1.readlines():
    try:
        j = line.split(",")
        arr = []
        j[-1] = j[-1][:-1]
        for i in j:
            i = dic[i]
            arr.append(i)
        arr.sort()
        #print(arr)
        for i in arr:
            f2.write(str(i))
            f2.write(" ")
        f2.write('\n')
    except:
        continue