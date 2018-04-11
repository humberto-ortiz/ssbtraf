## chunk.py - read in sbot feed, print out author, timestamp of private messages
## Copyright 2018 - Humberto Ortiz-Zuazaga - humberto.ortiz@upr.edu
## Released under the GNU General Public License version 3
## https://www.gnu.org/licenses/gpl-3.0.en.html

## This is python 3 code

## can read sbot feed from standard input:
## sbot feed | tail -n 1000 | python chunk.py

import json
import fileinput


# see https://stackoverflow.com/questions/20400818/python-trying-to-deserialize-multiple-json-objects-in-a-file-with-each-object-s

def load_json_multiple(segments):
    chunk = ""
    for segment in segments:
        chunk += segment
        try:
            yield json.loads(chunk)
            chunk = ""
        except ValueError:
            pass

types = {}

with fileinput.input() as f:
   for parsed_json in load_json_multiple(f):
       value = parsed_json['value']
       if "content" in value and "type" in value['content']:
               type = value['content']['type']
               if (type not in types):
                       types[type] = 1
                       print (type)

# looks like timestamps are in milliseconds (javascript)
# >>> datetime.datetime.fromtimestamp(1438958104164/1000.0)
# datetime.datetime(2015, 8, 7, 10, 35, 4, 164000)
