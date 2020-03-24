#!/usr/bin/env python

import sys
import os.path
import re
import json
import numpy as np
from tqdm import tqdm
import igraph as ig


def check_symmetric(a, rtol=1e-05, atol=1e-08):
	return np.allclose(a, a.T, rtol=rtol, atol=atol)

def isFloat(value):
	if(value is None):
		return False
	try:
		numericValue = float(value)
		return np.isfinite(numericValue)
	except ValueError:
		return False

def loadCSVMatrix(filename):
	return np.loadtxt(filename,delimiter=",")


configFilename = "config.json"
argCount = len(sys.argv)
if(argCount > 1):
		configFilename = sys.argv[1]

outputDirectory = "output"
csvOutputDirectory = os.path.join(outputDirectory, "csv")

if(not os.path.exists(outputDirectory)):
		os.makedirs(outputDirectory)

if(not os.path.exists(csvOutputDirectory)):
		os.makedirs(csvOutputDirectory)

with open(configFilename, "r") as fd:
		config = json.load(fd)

# "index": "data/index.json",
# "label": "data/label.json",
# "csv": "data/csv",
# "transform":"absolute", //"absolute" or "signed"
# "retain-weights":false,
# "threshold": "none"

indexFilename = config["index"]
labelFilename = config["label"]
CSVDirectory = config["csv"]

useAbsoluteValue = False
useSeparatedSigned = False
if(config["transform"].lower() == "absolute"):
	useAbsoluteValue = True
elif(config["transform"].lower() == "separated"):
	useSeparatedSigned = True

useThreshold = False
threshold = 0.0
if("threshold" in config and isFloat(config["threshold"])):
	useThreshold=True
	threshold = float(config["threshold"])

retainWeights = False
if("retain-weights" in config and config["retain-weights"]):
	retainWeights = True

with open(indexFilename, "r") as fd:
	indexData = json.load(fd)

with open(labelFilename, "r") as fd:
	labelData = json.load(fd)


for entry in indexData:
	entryFilename = entry["filename"]

	alreadySigned = ("separated-sign" in entry) and entry["separated-sign"]

	#inputfile,outputfile,signedOrNot
	filenames = [(entryFilename,entryFilename,False)]
	baseName,extension = os.path.splitext(entryFilename)

	if(alreadySigned):
		filenames += [(baseName+"_negative%s"%(extension),baseName+"_negative%s"%(extension),False)]
	elif(useSeparatedSigned):
		filenames += [(entryFilename,baseName+"_negative%s"%(extension),True)]
		entry["separated-sign"] = True

	if("null-models" in entry):
		nullCount = int(entry["null-models"])
		filenames += [(baseName+"-null_%d%s"%(i,extension),baseName+"-null_%d%s"%(i,extension),False) for i in range(nullCount)]
		if(alreadySigned):
			filenames += [(baseName+"_negative-null_%d%s"%(i,extension),baseName+"_negative-null_%d%s"%(i,extension),False) for i in range(nullCount)]
		elif(useSeparatedSigned):
			filenames += [(baseName+"-null_%d%s"%(i,extension),baseName+"_negative-null_%d%s"%(i,extension),True) for i in range(nullCount)]


	for filename,outputFilename,signed in tqdm(filenames):
		adjacencyMatrix = loadCSVMatrix(os.path.join(CSVDirectory, filename))
		directionMode=ig.ADJ_DIRECTED
		if(signed):
			adjacencyMatrix = -adjacencyMatrix
		if(useSeparatedSigned):
			adjacencyMatrix[adjacencyMatrix<=0] = 0
		if(useAbsoluteValue):
			adjacencyMatrix = np.abs(adjacencyMatrix)
		if(useThreshold):
			adjacencyMatrix[adjacencyMatrix<=threshold] = 0
		weights = adjacencyMatrix
		if(check_symmetric(adjacencyMatrix)):
			directionMode=ig.ADJ_UPPER
			weights = weights[np.triu_indices(weights.shape[0], k = 0)]
		g = ig.Graph.Adjacency((adjacencyMatrix > 0).tolist(), directionMode)
		if(retainWeights):
			g.es['weight'] = weights[weights > 0]
		
		
		with open(os.path.join(csvOutputDirectory,os.path.basename(outputFilename)), "w") as fd:
			if(retainWeights):
				outputData = g.get_adjacency(attribute='weight').data
			else:
				outputData = g.get_adjacency().data
			
			np.savetxt(fd,outputData,delimiter=",")

with open(os.path.join(outputDirectory,"index,json"), "w") as fd:
	json.dump(indexData,fd)

with open(os.path.join(outputDirectory,"label,json"), "w") as fd:
	json.dump(labelData,fd)

