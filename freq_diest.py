#! /usr/bin/env python 
#################
#Dylan Guldy    #
#Cryptogropy    #
#Doctor Craver  #
#Homework 1     #
#################
#############################################################
#This program takes a file converted to hex form and finds  #
#   the frequency distribution of the values                #
#File was obtained by the vim command :r !xxd -i file name, #
#   then stripping all new lines, commas, and double spaces #
#############################################################
    
import sys
import numpy as np
import matplotlib.pyplot as plt
hex_name = sys.argv[1]
hex_file = open(hex_name)
hex_file = hex_file.read()
hex_file = list(hex_file) 
hex_vals = {}
hex_counts = []

for val in hex_file:
    if val in hex_vals:
        print "%s, " % val
        hex_vals[val] = hex_vals[val]+1
#    elif "\n" in val:
#        temp_val = val.replace("\n","")
#        hex_vals[temp_val] = hex_vals[temp_val]+1
    else:
        hex_vals[val] = 1

hex_keys = hex_vals.keys()
hex_keys.sort()
for key in hex_keys:
    print "%s : %d" % (key, hex_vals[key])

for key in hex_keys:
    hex_counts.append(hex_vals[key])
pos = np.arange(len(hex_keys))
width = 1.0
ax = plt.axes()
ax.set_xticks(pos+(width/2))
ax.set_xticklabels(hex_keys)
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
plt.bar(pos, hex_counts, width, color='r')
plt.show()
