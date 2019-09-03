#! /usr/bin/python3

import os
import subprocess


MOVDIR = "/data/Movies/"
OUTDIR = "/data/"
SUBDIR = "/data/Subtitles/"

mkvmovies = [mov for mov in os.listdir(MOVDIR) if mov[-4:] == ".mkv"]

for mkv in mkvmovies:

    infile = MOVDIR + mkv
    trackids = list()
    languages = list()
    codecs = list()
    tracktypes = list()
    extrcommand = ["mkvextract", infile, "tracks"]

    summary = subprocess.run(
        ["mkvinfo", infile], capture_output=True, text=True)
    info = summary.stdout.split("\n")

    for row in info:
        if "Track number" in row:
            trackids.append(int(row[-3:-1]))
        elif "Language:" in row:
            languages.append(row[-3:])
        elif "Codec ID" in row:
            codecs.append(row.split(":")[-1].strip())
        elif "Track type" in row:
            tracktypes.append(row.split(":")[-1].strip())

    for trid, lang, cod, ttype in zip(trackids, languages, codecs, tracktypes):
        if ttype != "subtitles":
            continue
        outfile = SUBDIR + mkv[:-3] + lang
        if cod == "S_VOBSUB":
            outfile += ".sub"
        elif cod == "S_HDMV/PGS":
            outfile += ".sup"
        elif ttype != "S_TEXT/ASS":
            outfile += ".ass"
        else:
            print("Cannot extract subtitles for: {}".format(infile))
        extrcommand.append("{}:{}".format(trid, outfile))

    if len(extrcommand) > 3:
        subprocess.run(extrcommand)
        subprocess.run(
            ["mkvmerge", "-o", OUTDIR + mkv, "--no-subtitles", MOVDIR + mkv])
