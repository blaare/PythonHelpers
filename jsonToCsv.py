import json
import csv
import sys



def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

#FileName First in commandline
filename = sys.argv[1]

#output file Second in commandline
outfile = sys.argv[2]
data = open(filename,'r').read()
data = byteify(json.loads(data))
result = open(outfile, 'w')
csvwriter = csv.writer(result, dialect='excel')
count = 0
for piece in data:
      if count == 0:
             header = piece.keys()
             csvwriter.writerow(header)
             count += 1
      csvwriter.writerow(piece.values())
result.close()
