from testTools.tspInstanceParser import parseFile
import testSolvers.tspEvo as evo


nodes = []

f = open('testCases/berlin52.txt', 'r')
p = parseFile(f)

nodes = p[1]['nodes']

