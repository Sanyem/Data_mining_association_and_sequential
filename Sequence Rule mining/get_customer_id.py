f1 = open("online_retail.csv","r")
f2 = open("unique_customer_id.txt","w")
l = f1.readline()
c = set()
for line in f1.readlines():
    j = line.split(",")
    c.add(j[-2])
print(c)
for j in c:
    f2.write(j)
    f2.write("\n")