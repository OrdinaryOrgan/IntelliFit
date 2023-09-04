import csv
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--datadir", default="./data", help="path to data directory") 
parser.add_argument("--filename", default="data_pos.csv", help="input csv filename")
parser.add_argument("--labelvalue", default=1, help="the label value attached")
args = parser.parse_args()

data_dir = args.datadir
filename = args.filename
label = args.labelvalue
filepath = os.path.join(data_dir, filename)

with open(filepath,'r') as f:
    reader = csv.reader(f)
    rows = [row for row in reader if row]

header = rows[0]
header.append('label')

for row in rows[1:]:
    row.append(label)
    
with open(filepath,'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in rows:
        if row: 
            writer.writerow(row)