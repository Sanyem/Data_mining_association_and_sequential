from fp_growth import find_frequent_itemsets
import csv
f1 = open("transactions_item_id.csv","r")
minsup = 50
f_name = "frequent_itemsets_support_" + str(minsup) + ".csv"
f2=open(f_name,"w")
transactions=[]
for line in f1.readlines():
    line_arr = line.split(',')
    transactions.append(line_arr)
w = csv.writer(f2,delimiter=',')
for itemset in find_frequent_itemsets(transactions, minsup):
    w.writerow(itemset)