#!/usr/bin/env python3

from argparse import ArgumentParser
import json
import sys

arg_parser = ArgumentParser(description="Generate README.md based on a JSON file with songs")
arg_parser.add_argument("json_file", help="The JSON file for getting the data")
arg_parser.add_argument("template_file", help="The template file for generating the output")
arg_parser.add_argument("output_file", help="The output file")
args = arg_parser.parse_args()

# Open the JSON file
try:
    with open(args.json_file, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error: {type(e).__name__}: {e}", file=sys.stderr)
    sys.exit(1)

if not isinstance(data, dict):
    print("Error: JSON data is not an object")
    sys.exit(1)

artist = data.get("artistName", None)
print(f"Artist: {artist}")

songs = data.get("songs", None)
if songs is None:
    print("Error: The property \"songs\" was not found")
    sys.exit(1)
if not isinstance(songs, list):
    print("Error: The property \"songs\" is not a list")
    sys.exit(1)

# Open the template file
try:
    with open(args.template_file, "r", encoding="utf-8") as template_file:
        template_data = template_file.read()
except (FileNotFoundError):
    print(f"Error: {type(e).__name__}: {e}", file=sys.stderr)
    sys.exit(1)


# Generate Markdown table
# ==================================================================================================

markdown_table_lines = [
    "| Upload date | License | Number | Song name |",
    "|-------------|---------|--------|-----------|",
]
footnoteCount = 0
for song in songs:
    # Release date
    date = song["releaseDate"]
    # License
    license = song["license"]
    # URL
    url = song["originalUrl"]
    # Name
    name = song["name"]

    # (optional) Suffix and featuring artist
    suffix = song.get("suffix")
    feat = song.get("feat")
    # (optional) NEFFEX's release number
    number = song.get("neffexReleaseNumber")
    # (optional) Additional note
    note = song.get("additionalNote")

    # Prepare the final name
    final_name = name
    if feat is not None:
        final_name += f" (feat. {feat})"
    if suffix is not None:
        final_name += f" ({suffix})"

    # Prepare the name column content
    name_col = f"[{final_name}]({url})"
    if note is not None:
        footnoteCount += 1
        name_col += f"[^{footnoteCount}]"

    number_col = number if number is not None else "_none_"

    line = f"| {date:<11} | {license:<7} | {number_col:<6} | {name_col} |"
    markdown_table_lines.append(line)

markdown_table_data = "\n".join(markdown_table_lines)


# Generate footnotes
# ==================================================================================================

markdown_footnotes = []
songs_with_footnotes = (song for song in songs if "additionalNote" in song)
for n, song in enumerate(songs_with_footnotes, 1):
    footnote = f"[^{n}]: {song["additionalNote"]}\n"
    markdown_footnotes.append(footnote)

markdown_footnotes_data = "\n".join(markdown_footnotes)


# Replace template
# ==================================================================================================

songs_table_text_placeholder="SONGS_MARKDOWN_TABLE"
if songs_table_text_placeholder not in template_data:
    print(f"Error: the string '{songs_table_text_placeholder}' was not found in template")
    sys.exit(1)

songs_footnotes_text_placeholder="SONGS_MARKDOWN_FOOTNOTES"
if songs_footnotes_text_placeholder not in template_data:
    print(f"Error: the string '{songs_footnotes_text_placeholder}' was not found in template")
    sys.exit(1)

output_data = template_data
output_data = output_data.replace(songs_table_text_placeholder, markdown_table_data)
output_data = output_data.replace(songs_footnotes_text_placeholder, markdown_footnotes_data)


# Open the output file
with open(args.output_file, "w", encoding="utf-8") as output_file:
    output_file.write(output_data)
