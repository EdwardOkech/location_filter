#!/usr/bin/env python

import sys
reload(sys)    # to re-enable sys.setdefaultencoding()
sys.setdefaultencoding('utf-8')

import json

path = sys.argv[1]

#the json file we want to read
infile = open("kaboong-locs.json", "r")
#the json file we will be outputing
#outfile = open("filtered.json","w")

#basicly the location/district we want to filter
# keywords = ['Sool / Laas Caanood','Sool / Taleex', 'Sool / Taleex', 'Sool / Xudun', 'Sool / Lasanod', 'Sool / Lasanod',
# 'Sool / Ainabo','Sool / Caynabo']

keyword = 'Kaabong /'
# f = json.write(outfile)
#log number of areas processed
processed_areas = 0
skipped_areas = 0

#output = []
with open(path, "w") as outfile:
	for line in json.loads(infile.read()):
		try:
			a = line.get('area')
			if a.startswith(keyword):
				processed_areas += 1
				# helps to see the line output on the terminal as it writes on the file ;)
				print json.dumps(line,sort_keys=True,indent=4, separators=(',', ': '))
				#output.append(line)
				json.dump(line, outfile,sort_keys=True, indent=4, separators=(',',': '))
		except Exception as e:
			print(e)
			skipped_areas += 1
			continue

print('number of processed areas: {0}'.format(processed_areas))
# print('number of areas skipped:{0}'.format(skipped_areas))
print('Done..!!!')
