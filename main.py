#!/usr/bin/env python3

import os
import json

jsondata = {}
stop = False

# filepath = "E:\Oliver\oliver_drive\Programmieren\python\py_obsidian"
# filepath = "/mnt/c/Users/Oliver/Desktop/Chem"
obsidianPath = "E:\Oliver\oliver_drive\zettelkasten\.obsidian"
directory = "obsidian-graphview-presets"

pathtoplugins = obsidianPath + "\plugins"
plugindir = pathtoplugins + "\\" + directory


def setupPlugindir():
    try:
        os.mkdir(os.path.join(pathtoplugins, directory))
        print("Directory '% s' created" % directory)

    except FileExistsError:  # not really an error
        print("Pluginfolder exists")


def readGraphsettings():
    # read the graphsettings form file
    try:
        # Opening JSON file
        with open(obsidianPath + "\graph.json", 'r', encoding='UTF-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Graphfile not found")


def storeGraphsettings(settings):
    # save actual settings
    with open(plugindir + "\data.json", 'w+') as f:
        json.dump(jsondata, f)


def loadsettings(name):
    # read data
    with open(plugindir + "\data.json", 'r') as f:
        data = json.load(f)

    for i in range(len(data)):
        redname = data.get(str(i)).get("name")
        if redname == name:
            return data.get(str(i)).get("settings")


def loadGraphsettings(settings):
    with open(obsidianPath + "\graph.json", 'w', encoding='UTF-8') as f:
        json.dump(settings, f)


while not stop:
    try:
        mode = int(input("Was möchtest du machen? \n save settings: 1\n load settings: 2\n Beenden: 3\n"))

    except:
        print("ERROR")
        continue

    if mode == 1:
        name = input("Gib einen Namen ein:")
        setg = readGraphsettings()
        jsondata[0] = {"name": name, "settings": setg}  # FIXME
        storeGraphsettings(setg)
    elif mode == 2:
        name = input("Gib den Namen ein: ") #TODO check if aviable
        setg = loadsettings(name)
        loadGraphsettings(setg)
    elif mode == 3:
        stop = True
        print("Das Programm wird beendet")
    else:
        print("undefined action")

# print(json.dumps(jsondata, indent=4))


set = loadsettings("firstname")

loadGraphsettings(set)
