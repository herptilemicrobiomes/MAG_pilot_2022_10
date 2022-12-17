#!/usr/bin/env python3

import argparse
import os
import re
import csv

parser = argparse.ArgumentParser(
    prog='summarize_bin_depth.py', description='generate table of bin avg depth')

parser.add_argument('-d', '--dir', required=True, type=str,
                    help='Sample folder in results from metashot run')

args = parser.parse_args()

name = os.path.basename(args.dir)

bindir = os.path.join(args.dir,'bins')
metabatdepth = os.path.join(args.dir,'metabat2',name,'depth.txt')

fastapattern = re.compile(r'^>(\S+)')
contigs2bin = {}
depths = {}
for binfile in os.listdir(bindir):
    bin = binfile[0:-3]
    depths[bin] = []
    # print('bin is',bin)
    with open(os.path.join(bindir,binfile),"r") as fh:
        for line in fh:
            m = fastapattern.match(line)
            if m:
                contigs2bin[m.group(1)] = bin

with open(metabatdepth,"r") as fh:
    depthfh = csv.reader(fh, delimiter='\t')
    header = next(depthfh)

    for row in depthfh:
        ctg = row[0]
        dp  = float(row[2])
        if ctg in contigs2bin:
            depths[contigs2bin[ctg]].append(dp)

print("\t".join(['BIN','NUM_CONTIGS','MEAN_DEPTH']))
for bin in sorted(depths):
    sumtotal = sum(depths[bin])
    n   = len(depths[bin])
    print("%s\t%d\t%.2f"%(bin,n,sumtotal/n))
