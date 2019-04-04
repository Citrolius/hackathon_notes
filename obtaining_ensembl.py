#!/usr/bin/python

#bring python3 print() into python2
from __future__ import print_function
import os, math, traceback, datetime, urllib, requests, json, argparse, sys

def geteff():
	with open(threshfile, "w") as fthresh:
		for line in fthresh:
			col = line.split("\t")
			chrom = col[1]
			bp = col[2]
			server = "http://rest.ensemblgenomes.org"
			ext = "/overlap/region/oryza_sativa/{}:{}-{}:1?feature=variation".format(chrom, bp, bp)

			r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})

			if not r.ok:
				r.raise_for_status()
				sys.exit()

			decoded = r.json()
			info=repr(decoded)
			print(type(info))
            
if __name__ == "__main__":  
    geteff()