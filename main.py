#!/usr/bin/env python

import sys
import os.path
from enum import Enum
from os.path import join as PJ
from collections import OrderedDict
import re
import json
import numpy as np
from tqdm import tqdm
import igraph as ig
import jgf

def isFloat(value):
	if(value is None):
		return False
	try:
		numericValue = float(value)
		return np.isfinite(numericValue)
	except ValueError:
		return False

configFilename = "config.json"
argCount = len(sys.argv)
if(argCount > 1):
		configFilename = sys.argv[1]

outputDirectory = "output"
outputFile = PJ(outputDirectory,"network.json.gz")

if(not os.path.exists(outputDirectory)):
		os.makedirs(outputDirectory)

with open(configFilename, "r") as fd:
		config = json.load(fd)


# "network":"data/network.json.gz"
# "transform":"absolute", //"absolute", "positive", "negative", "layered"
# "retain-weights":false,
# "threshold": "none"
# "percentile": "none"
# "strict-percentile": false
# "selection-transform": "none" //"none","absolute", "positive", "negative"
# "keep-zero-weights": false

class transformType(Enum):
	none = 0
	absolute = 1
	positive = 2
	negative = 3
	layered = 4


transform = None
if("transform" in config):
	if(config["transform"].lower() == "absolute"):
		transform = transformType.absolute
	elif(config["transform"].lower() == "positive"):
		transform = transformType.positive
	elif(config["transform"].lower() == "negative"):
		transform = transformType.negative
	elif(config["transform"].lower() == "layered"):
		transform = transformType.layered

selectionTransform = None
if("selection-transform" in config):
	if(config["selection-transform"].lower() == "absolute"):
		selectionTransform = transformType.absolute
	elif(config["selection-transform"].lower() == "positive"):
		selectionTransform = transformType.positive
	elif(config["selection-transform"].lower() == "negative"):
		selectionTransform = transformType.negative
	elif(config["selection-transform"].lower() == "none"):
		selectionTransform = transformType.none

if(selectionTransform is None):
	if(transform == transformType.layered):
		selectionTransform = transformType.absolute
	else:
		selectionTransform = transform



useThreshold = False
threshold = 0.0
if("threshold" in config and isFloat(config["threshold"])):
	useThreshold=True
	threshold = float(config["threshold"])

usePercentile = False
percentile = 0.0
if("percentile" in config and isFloat(config["percentile"])):
	usePercentile=True
	percentile = float(config["percentile"])

	strictPercentile = False
	if("strict-percentile" in config and config["strict-percentile"] is not None):
		strictPercentile = config["strict-percentile"]


retainWeights = False
if("retain-weights" in config and config["retain-weights"] is not None):
	retainWeights = config["retain-weights"]


keepZeroWeight = False
if("keep-zero-weights" in config and config["keep-zero-weights"] is not None):
	keepZeroWeight = config["keep-zero-weights"]


networks = jgf.igraph.load(config["network"],compressed=True)

outputNetworks = []
for network in networks:
	originalEdgeCount = network.ecount()
	if("weight" in network.edge_attributes() and originalEdgeCount>0):
		
		if(transform == transformType.absolute):
			weights = np.abs(network.es["weight"])
		elif(transform == transformType.positive):
			weights = np.array(network.es["weight"])
			weights[weights<0] = 0
		elif(transform == transformType.negative):
			weights = -np.array(network.es["weight"])
			weights[weights<0] = 0
		else:
			weights = np.array(network.es["weight"])
		
		
		if(selectionTransform == transformType.absolute):
			selectionWeights = np.abs(network.es["weight"])
		elif(selectionTransform == transformType.positive):
			selectionWeights = np.array(network.es["weight"])
			selectionWeights[selectionWeights<0] = 0
		elif(selectionTransform == transformType.negative):
			selectionWeights = -np.array(network.es["weight"])
			selectionWeights[selectionWeights<0] = 0
		else:
			selectionWeights = np.array(network.es["weight"])
		

		if(not keepZeroWeight):
			edgesSelection = (weights!=0)+(selectionWeights!=0)
		else:
			edgesSelection = np.ones(originalEdgeCount,dtype=np.bool)

		
		if(useThreshold):
			edgesSelection *= (selectionWeights>=threshold)
		
		remainingEdgesCount = np.sum(edgesSelection)

		if(usePercentile and remainingEdgesCount>0):
				if(strictPercentile):
						sortedIndices = sorted(np.arange(originalEdgeCount), key=lambda i: selectionWeights[i],reverse=True)
						topIndices = sortedIndices[int(round((1.0-percentile)*remainingEdgesCount)):]
						edgesPercentileSelection = np.zeros(originalEdgeCount,dtype=np.bool)
						edgesPercentileSelection[topIndices] = True
						edgesSelection *= edgesPercentileSelection
				else:
					quantileThreshold = np.quantile(selectionWeights[edgesSelection],1.0-percentile)
					edgesSelection *= (selectionWeights>=quantileThreshold)
		
		edgesToBeRemoved = np.where(~edgesSelection)[0]

		if(transform == transformType.layered):
			network.es["layer"] = [0 if weight>0 else 1 for weight in weights]
		
		if(retainWeights):
			network.es["weight"] = weights
		else:
			del network.es["weight"]
			
		network.delete_edges(edgesToBeRemoved)

	outputNetworks.append(network)

jgf.igraph.save(outputNetworks,outputFile,compressed=True)
