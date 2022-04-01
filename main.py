#!/usr/bin/env python3

import os
import json

jsondata = {}

obsidianPath = "E:\Oliver\oliver_drive\zettelkasten\.obsidian"
directory = "obsidian-graphview-presets"

pathtoplugins = obsidianPath + "\plugins"
plugindir = pathtoplugins + "\\" + directory


def setupPlugindir():
    print('TODO')

def readGraphsettings():
    print('TODO')

def storeGraphsettings(settings):
    print('TODO')

def getstoredsettings(name):
    print('TODO')

def loadGraphsettings(settings):
    print('TODO')


try:
    os.mkdir(os.path.join(pathtoplugins, directory))
    print("Directory '% s' created" % directory)

except FileExistsError: # not really an error
    print("Pluginfolder exists")

# read the graphsettings form file
try:
    # Opening JSON file
    with open(obsidianPath + "\graph.json", 'r', encoding='UTF-8') as f:
        actsettings = json.load(f)

except FileNotFoundError:
    print("Graphfile not found")

jsondata[0] = {"name": "firstname", "settings": actsettings}

print(json.dumps(jsondata, indent=4))

# save actual settings
with open(plugindir + "\data.json", 'w+') as f:
    json.dump(jsondata, f)


# read data
with open(plugindir + "\data.json", 'r') as f:
    data = json.load(f)



