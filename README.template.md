# NEFFEX song list

Extracted from [NEFFEX YouTube channel](https://www.youtube.com/@neffexmusic)
using [YT-DLP](https://github.com/yt-dlp/yt-dlp):

```
yt-dlp --no-flat-playlist --no-download --print-to-file \
    "| %(upload_date>%Y-%m-%d)s | [%(title)s](https://youtu.be/%(id)s) |" \
    neffex_channel.txt \
    https://www.youtube.com/@neffexmusic/videos
```

| License | Description |
|---------|-------------|
| [CC BY](https://creativecommons.org/licenses/by/3.0/legalcode) | royalty-free |
| [LABEL](https://www.wmg.com/faq) | rights are restricted by a record label |
| [REMIX](https://www.theverge.com/2019/5/24/18635904/copyright-youtube-creators-dmca-takedown-fair-use-music-cover) | rights may be restricted by original artist's record label |

SONGS_MARKDOWN_TABLE

SONGS_MARKDOWN_FOOTNOTES
