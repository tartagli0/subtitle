#!/bin/python3

import os
import subprocess
import sys


allfiles = os.listdir("data")
allfiles.sort()

vidsrt = list()

for idx in range(len(allfiles) - 1):

    if allfiles[idx][-4:] != ".srt":
        continue

    cur = allfiles[idx]
    nex = allfiles[idx + 1]
    cur_adj = cur.split(".")[0]
    nex_adj = nex.split(".")[0]

    if cur_adj == nex_adj:
        vidsrt.append((cur, nex))
    elif idx > 0:
        pre = allfiles[idx - 1]
        pre_adj = pre.split(".")[0]
        if cur_adj == pre_adj:
            vidsrt.append((cur, pre))

for comb in vidsrt:

    subpath = "data/" + comb[0]
    vidpath = "data/" + comb[1]
    outpath = "synced_subs/" + comb[0]
    command = ["subsync", "--cli",
               "sync", "--sub", subpath, "--ref", vidpath, "--out", outpath]

    if "Downfall" in comb[0]:
        command.extend(["--sub-lang", "eng", "--ref-lang", "ger"])
    elif comb[0].split(".")[0] in ["Motorcycle_Diaries", "Open_Your_Eyes"]:
        command.extend(["--sub-lang", "eng", "--ref-lang", "spa"])

    results = subprocess.run(
        command, capture_output=True, text=True, universal_newlines=True)

    if results.stderr != "":
        print(results.stderr)

    if results.stdout != "":
        print(results.stdout)

    sys.stderr.flush()
    sys.stdout.flush()
