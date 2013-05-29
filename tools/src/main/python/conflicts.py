import sys, re
import csv
import mimeparse
from utils import *


tsv_file = csv.reader(CommentedFile(open(sys.argv[1], "rb")), delimiter='\t')
    	
dst = {}
for row in tsv_file:
    #print row
    try:
        (fmtS, fmtT, fmtD, year, count) = row
    except:
        print "ERROR: Could not load ",row
        continue

    
    # Include the version info when comparing
    version = True    

    # Normalise, lower case and no space after the ;
    fmtSr = reduceType(fmtS,version)
    fmtTr = reduceType(fmtT,version)
    fmtDr = reduceType(fmtD,version)

    # Only report when the base type disagrees, ignore parameters:
    if fmtDr != fmtTr:
    #if fmtTr == "application/octet-stream" and fmtDr == "application/octet-stream":
    #if True:
        #print fmtS,fmtT,fmtD
        #combo = "{}\t{}\t{}".format(fmtSr,fmtTr,fmtDr)
        #combo = "{}\t{}".format(fmtSr,fmtTr)
        combo = "{}\t{}".format(fmtTr,fmtDr)
        if not combo in dst:
            dst[combo] = 0
        dst[combo] += int(count)

#print "Server Type\tTika Type\tDROID Type\tCount"
print "Tika Type\tDROID Type\tCount"
for fmt in sorted(dst):
    print "{}\t{}".format(fmt,dst[fmt])

