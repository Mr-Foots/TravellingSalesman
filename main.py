import time
import os

import Algorithms.tspEvo as evo
import Algorithms.tspGreedy as greedy
import Algorithms.testBrute as brute
ALGORITHMS = [evo, brute, greedy]
DATA_SETS = {'1':'5.txt','2':'10.txt','3':'13.txt','4':'29.txt','5':'52.txt','6':'100.txt','7':'200.txt','8':'439.txt'}

def cal_distance(p1, p2):
    #calculates distance from two points
    return int((((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2))**.5)

def averages(times, costs, trial_number):
    avg_cost = sum(costs)/trial_number
    avg_time = sum(times)/trial_number

    return avg_cost, avg_time

def data_parse(data_file = 'data/29.txt'):
    distance_matrix = {}
    Nodes = {}
    data = open(data_file, 'r')

    for line in data:
        raw_line = line.split()
        Nodes[int(raw_line[0])] = (int(float(raw_line[1])),int(float(raw_line[2])))

    for current in list(Nodes.keys()):
        distances = {}
        for node in Nodes:
            if node != current:
                distances[node] = cal_distance(Nodes[current], Nodes[node])
            else:
                distances[node] = 0

        distance_matrix[current] = distances

    return distance_matrix


costs = []
times = []
trial_number = 1

os.system('cls')
print('Algorithm Control\n')
print('''

1------Genetic Algorithm
2------Brute Force Algorithm
3------Greedy Algorithm

''')

ans = int(input('Choose program to run: \n\n'))
print("""
Data Sets:

1------5 Nodes
2------10 Nodes
3------13 Nodes
4------29 Nodes
5------52 Nodes
6------100 Nodes
7------200 Nodes
8------439 Nodes

""")
ans_ds = input("Choose Data Set: ")
if ans_ds == '':
    ans_ds = '2'

distance_matrix = data_parse('data/' + DATA_SETS[ans_ds])

for trial in range(trial_number):
    start_time = time.perf_counter()
    costs.append(ALGORITHMS[ans-1].main(distance_matrix))
    print("Time Elapsed: ", time.perf_counter() - start_time)
    #print('Trial ', str(trial))

#avg_cost, avg_time = averages(times, costs,trial_number)
#print('\n')
#print("Average Cost: ", avg_cost)
#print('Average Time: ', avg_time)
