from operator import itemgetter
from itertools import groupby
f1 = open("sequence_data.txt","r")
f2 = open("sequence_data_final.txt","w")
for line in f1.readlines():
    l = line.split()
    k=list(map(itemgetter(0), groupby(l)))
    for i in k:
        f2.write(i)
        f2.write(" ")
    f2.write("\n")