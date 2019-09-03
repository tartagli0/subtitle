# Automatically Download Subtitles
The [OpenSubtitlesDownload](https://github.com/emericg/OpenSubtitlesDownload)
Python script attempts to automatically match and download corresponding
subtitles for a movie. See the
[CLI Wiki](https://github.com/emericg/OpenSubtitlesDownload/wiki/Usage-as-a-CLI-script)
for documentation.

The *bash* code below will download subtitles for multiple files:
```bash
for movie in /data/Movies/*; do
  ./OpenSubtitlesDownload.py --cli --auto --search filename "${movie}" --output "/data/Movies"
done
```
