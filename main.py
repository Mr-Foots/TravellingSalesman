import timeit
import os
import Algorithms.tspEvo as evo
import Algorithms.tspBrute as brute


os.system('cls')
Nodes = {}
data = open('data.txt', 'r')

for line in data:
    i = line.split()
    Nodes[i[0]] = (int(float(i[1])),int(float(i[2])))

print('Nodes Created Successfully!')
print('''

1------Genetic Algorithm
2------Brute Force Algorithm
''')
ans = input('Choose program to run: \n')
instanceSize = int(input('Choose the number of Nodes: \n'))




if ans == '1':
    evo.main(Nodes, instanceSize)
elif ans == '2':
    brute.main(Nodes, instanceSize)
