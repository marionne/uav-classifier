import json
import codecs

from pprint import pprint

#with codecs.open('testing0.json', encoding='utf-8') as f:
#	data = json.loads(f.read())
#pprint(data)

data = []
with codecs.open('testing0.json','rU','utf-8') as f:
    for line in f:
       data = data.append(json.loads(line))
pprint(data)
