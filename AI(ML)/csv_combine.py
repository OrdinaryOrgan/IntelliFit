import csv
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--datadir", default="./data", help="path to data directory") 
parser.add_argument("--pos_sample", default="data_pos.csv", help="input pos csv filename")
parser.add_argument("--neg_sample", default="data_neg.csv", help="input neg csv filename")
args = parser.parse_args()

data_dir = args.datadir

neg_file = args.neg_sample
pos_file = args.pos_sample

neg_path = os.path.join(data_dir, neg_file)
pos_path = os.path.join(data_dir, pos_file)

combined_path = os.path.join(data_dir, 'combined_data.csv')

with open(neg_path, 'r') as neg, open(pos_path, 'r') as pos:

    neg_reader = csv.reader(neg)
    pos_reader = csv.reader(pos)

    with open(combined_path, 'w', newline='') as comb:
        
        comb_writer = csv.writer(comb)

        for row in neg_reader:
            comb_writer.writerow(row)
            
        for row in pos_reader:
            comb_writer.writerow(row)