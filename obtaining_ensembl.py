#!/usr/bin/python

#bring python3 print() into python2
from __future__ import print_function
import os, math, traceback, datetime, urllib, requests, json, argparse, sys

def geteff():
	'''This function parses SNPs above logP threshold and obtains their snp effects from ebi'''
	with open("Results_filtered_threshold.txt", "r") as fthresh:
		fthresh.readline()
		for line in fthresh:
			col = line.split("\t")
			chrom = col[1]
			bp = col[2]
			server = "http://rest.ensemblgenomes.org"
			ext = "/overlap/region/oryza_sativa/{}:{}-{}:1?feature=variation".format(chrom, bp, bp)

			r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
			#print(r, file="tmp.txt")

			if not r.ok:
				r.raise_for_status()
				sys.exit()

			decoded = r.json()
			info=repr(decoded)
			print(info)
			print(type(info))
            #extract the base change information and consequences.

def getgs():
	with open("Results_filtered_threshold.txt", "r") as fthresh:
		fthresh.readline()
		for line in fthresh:
			col = line.split("\t")
			chrom = col[1]
			bp = col[2]
			server = "http://rest.ensemblgenomes.org"
			ext = "/overlap/region/oryza_sativa/{}:{}-{}:1?feature=gene".format(chrom, bp, bp)

			r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
			#print(r, file="tmp.txt")

			if not r.ok:
				r.raise_for_status()
				sys.exit()

			decoded = r.json()
			info=repr(decoded)
			print(info)
			print(type(info))
            #extract the base change information and consequences.



if __name__ == "__main__":  
    geteff()