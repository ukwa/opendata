import sys, re
import csv
import mimeparse
from collections import defaultdict


# Need to count total links by year to use relative cut-off.
links = defaultdict(int)
tsv_file = csv.reader(open(sys.argv[1], "rb"), delimiter='\t')
for row in tsv_file:
    try:
        (yr, dst, src, count) = row
    except:
        print "ERROR: Could not load ",row
        continue
    links[yr] += int(count)

# Set up accumultors:
matrix = defaultdict(int)
domains = []
#domains.append("(other)")
years = []
ylinks = defaultdict(int)

tsv_file = csv.reader(open(sys.argv[1], "rb"), delimiter='\t')
for row in tsv_file:
    try:
        (yr, dst, src, count) = row
    except:
        print "ERROR: Could not load ",row
        continue
    
    # Only store large link categories
    count = int(count)
    if count/float(links[yr]) > 0.001:

        # Build up lists of the years and domains involved:    
        if not yr in years:
            years.append(yr)
        if not src in domains:
            domains.append(src)
        if not dst in domains:
            domains.append(dst)
        
        # Store the total counts for each combination
        key = (yr,src,dst)
        matrix[key] += count
        ylinks[yr] += count
        print "PRE",key,count/float(links[yr])

# Generate output file containing the matrix
fm = open("link-matrix.json",'w')
fm.write("{\n")
initm = False
for year in sorted(years):
    cols = []
    for src in sorted(domains):
        if src == None:
            continue
        row = []
        for dst in sorted(domains):
            if dst == None:
                continue
            key = (year,src,dst)
            total = matrix[key]/float(ylinks[year])
            #if total > 0:
            row.append(total)
        # Build up the matrix:
        cols.append( "[" + ",".join([str(x) for x in row]) + "]")
    # matrix:
    line = "[" + ",".join([str(x) for x in cols]) + "]"
    if initm == True:
        fm.write(",\n")
    fm.write( "\t\"{}\": {}".format(year, line) )
    if initm == False:
        initm = True
# and close
fm.write("\n}\n")
fm.close()

# Generate output file containing the index
fi = open('link-index.csv','w')
fi.write("name,color\n")

for src in sorted(domains):
    colour = '#444444'
    if src.endswith(".uk"):
        colour = "#880000"
    # Write the index
    fi.write("{},{}\n".format(src,colour))
# and close
fi.close()