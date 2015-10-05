

def parseFile(f):
	nodes = []
	attri = []
	final = []

	for line in f:

		lineAR = line.replace('\n', '').split(": ")
		if line == 'EOF':
			final.append({'attributes': attri})
			final.append({'nodes': nodes})
			return final

		elif len(lineAR) > 1:
			d = {lineAR[0]:lineAR[1]}
			attri.append(d)

		elif lineAR[0] != "NODE_COORD_SECTION":
			temp = line.replace('\n','').split(' ')
			node = {temp[0]: (float(temp[1]), float(temp[2]))}
			nodes.append(node)


			

