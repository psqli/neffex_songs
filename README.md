# NEFFEX song list

Extracted from [NEFFEX YouTube channel](https://www.youtube.com/@neffexmusic)
using [YT-DLP](https://github.com/yt-dlp/yt-dlp):

```
yt-dlp --no-flat-playlist --no-download --print-to-file \
    "| %(upload_date>%Y-%m-%d)s | [%(title)s](https://youtu.be/%(id)s) |" \
    neffex_channel.txt \
    https://www.youtube.com/@neffexmusic/videos
```
