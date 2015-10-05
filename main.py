from testTools.tspInstanceParser import parseFile
import testSolvers.tspBrute as brute
import testSolvers.tspEvo as evo
import testSolvers.tspHeur as heur


nodes = []

f = open('testCases/berlin52.txt', 'r')
p = parseFile(f)


nodes = p[1]['nodes']
brute.main(nodes)