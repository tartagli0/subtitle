# Automatically Download Subtitles
The [OpenSubtitlesDownload](https://github.com/emericg/OpenSubtitlesDownload)
Python script attempts to automatically match and download corresponding
subtitles for a movie from
[opensubtitles.org](https://www.opensubtitles.org/en/search). See the
[CLI Wiki](https://github.com/emericg/OpenSubtitlesDownload/wiki/Usage-as-a-CLI-script)
for documentation.

The *bash* code below will download subtitles for multiple files:
```bash
for movie in /data/Movies/*; do
  ./OpenSubtitlesDownload.py --cli --auto --search filename "${movie}" --output "/data/Movies"
done
```

# Sync Subtitles
The [SubSync](https://snapcraft.io/subsync) *snap* package automatically
synchronizes subtitles for a corresponding movie. CLI options for *SubSync*
are described in the project's
[Github Wiki page](https://github.com/sc0ty/subsync/wiki/Command-line-options).

## Use cases
To sync a single subtitle file to a movie, execute the command:
```bash
subsync --cli sync --sub subtitlefile.srt --ref moviefile.mkv
```

Synching multiple files can be accomplished via the *batch* option described
in the documentation. Synching multiple files, however, can cause the process
to exit with a *segmentation fault* error. One way to avoid this is to wrap
the process in a *Python* script such as
[syncall.py](https://github.com/tartagli0/subtitle/blob/master/syncall.py)
in this repo.

## Snap file access
*Snap* packages cannot access files outside of the */home/<user>/snap*
directory. In most cases, the media containing movies and subtitles should
be mounted to a folder within the *snap* directory. For example, to acess
files stored in a *samba* share, first mount the share:
```bash
mount -t cifs //192.168.50.178/Shared/Movies /home/abe/snap/data -o credentials=/home/abe/.smb
```

# Remove Image-based Subtitles from MKV
To remove existing image-based subtitles from MKV files, use
[mkvtoolnix](https://mkvtoolnix.download). To remove subtitles from a single
file, run the command:
```bash
mkvmerge -o newfile.mkv --no-subtitles oldfile.mkv
```

# Convert Image-based Subtitles to SRT
Before converstion to SRT, image-based subtitles (i.e., *PGS*, *VOBSUB*) must
be extracted from their corresponding *MKV* containers. This can be
accomplished with the *mkvinfo* and *mkvextract* commands included with
*mkvtoolnix*:
```bash
# Display details of MKV file
mkvinfo filename.mkv
# Extract English subtitles in PGS format
mkvextract moviename.mkv tracks 2:moviename.eng.sup
# Extract Spanish subtitles in *VOBSUB* format
mkvextract moviename.mkv tracks 2:moviename.spa.sub
```
A full description of subtitle formats and corresponding output file
types is available in the *mkvextract*
[documentation](https://mkvtoolnix.download/doc/mkvextract.html#mkvextract.output_file_formats).

## Bulk extraction
To extract subtitles from multiple files, a script such as
[mkvsub.py](https://github.com/tartagli0/subtitle/blob/master/mkvsub.py)
can be used.

## Conversion tools
Both *sup* and *sub* files can be converted to *SRT* format with the
Windows-based [SubtitleEdit](http://www.nikse.dk/subtitleedit) tool or the
web-based [Subtitle Tools](https://subtitletools.com).
