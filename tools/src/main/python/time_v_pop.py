import sys, re
import csv
from utils import *
from collections import defaultdict

tsv_file = csv.reader(CommentedFile(open(   sys.argv[1], "rb")), delimiter='\t')

ym = 17
floor = 0
floorfrac = 0.1/100.0
start = 0

nf = defaultdict(int)
nl = defaultdict(int)

for row in tsv_file:
    if start == 0:
        start = 1
        continue
    #print row
    ys = 0
    yt = 0
    tot = 0
    fy = 0
    ly = 0
    for yd in range(1,ym+1):
        tot += int(row[yd])
        if int(row[yd]) > floor:
            if ys == 0:
                ys = yd
                yt = 1
            else:
                yt = 1 + yd - ys
        if int(row[yd]) > 0 and fy == 0:
            fy = yd
        if int(row[yd]) > 0:
            ly = yd

    # Collect first found years:
    nf[fy] += 1
    # Collect last year found:
    nl[ly] += 1
    # Output timespans
    #if int(row[ym]) <= floor and int(row[ym-1]) <= floor:
    #if int(row[1]) <= floor and int(row[2]) <= floor and int(row[3]) <= floor:
    if yt > 0:
        if float(row[ym])/tot <= floorfrac and int(row[ym-1])/tot <= floorfrac:
            print "{}\t{}\t{}".format(row[0],yt,tot)

#print "Year\tFirst Observed\tLast Observed"
#for y in range(1,ym+1):
#    print "{}\t{}\t{}".format( y+1993, nf[y], nl[y] )
