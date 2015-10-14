#!/usr/bin/env python

import json
import argparse
import sys
import csv

# files are given on commandline

parser = argparse.ArgumentParser(description='Process json from dusti API')
parser.add_argument(metavar='J', type=str, nargs='+', dest='jsonfilenames',
                    help='json files to be processed')
parser.add_argument('-o', '--outfile', default=None, type=str, dest='outfile',
                    help='output filename (.csv), if not given print to stdout')

args = parser.parse_args()

csvfilename=args.outfile
if csvfilename is None:
    csvout=sys.stdout
else:
    csvout=open(csvfilename,'w')

printcsvheader=True
for jsonfilename in args.jsonfilenames:
    with open(jsonfilename) as f:
        j=json.load(f)
        for r in j['results']:
            csvdict={}
            csvdict['timestamp']=r['timestamp']
            for v in r['sensordatavalues']:
                csvdict[v['value_type']]=v['value']
            if printcsvheader:
                fieldnames=csvdict.keys()
                csvwriter = csv.DictWriter(csvout, fieldnames=csvdict.keys())
                csvwriter.writeheader()
                printcsvheader=False
            csvwriter.writerow(csvdict)

# close csvout file handler
csvout.close()
