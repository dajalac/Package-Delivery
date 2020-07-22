from hashTable import *
from package import Packages
import readPackages
h2 = MyHashTable(40)
for i in range(2):
    p = Packages(i, "address", "city", "status", "zip", "deadline", "kg", "notes", "delivery status")
    h2.add(p.package_id, p)
    p_returned2 = h2.search(p.package_id)
    print("search h2", p_returned2.package_id)

#r = h2.search(24)
#print("none should show",r) #todo should implement how to handle none in hash return

# test to see if it is reading the hash table with the packages
## aqui é como chama do readPackage
myH = readPackages.get_hash_table()
r2 = myH.search(40)
print("my package HAHAHA",r2.package_id)


#### get the distance
import csv

distance_list = []
with open('WGUPS_Distance_Table.csv', 'r') as csv_file:
    readCsv = csv.reader(csv_file, delimiter=',')
    print(readCsv)
    for row in readCsv:
        distance_list.append(row)
print(distance_list)

distance_dic = {"HUB": 0, " 1060 Dalton Ave S": 1, "1330 2100 S": 2}

### get the names
with open("address.csv", 'r')as n:
    names = csv.reader(n, delimiter=',')
    names = list(names)

print("names @@@@@@@", names[0][1])


# Dijkatra's
def dj(start_vertex):
    global vertx
    unvisited_queue = []
    for current_vertex in distance_list:
        unvisited_queue.append(current_vertex)

    # tira os ' ' = acho q n vou usar
    distance = []
    for row in distance_list:
        c = [i for i in row if i != '']
        distance.append(c)
    print(distance)

    min = 1000
    for i in range(len(unvisited_queue)):
        print("i", i)
        if distance_list[i][start_vertex] is '':  # here I think that we should use unvisited-quee
            continue  # tem q mudar isso p como esta no onenote
        elif 0 < float(distance_list[i][start_vertex]) <= float(min):
            min = distance_list[i][start_vertex]
            print("min distance 3", min)
            vertx = i
    print("vertexi", vertx)
    current_vertex = unvisited_queue.pop(vertx)
    print((current_vertex))
    # start_vertex= vertx
    print(current_vertex)


a = dj(3)

# start_vertex_distance = distance_list[start_vertex][start_vertex]


# while len(unvisited_queue) >0 :
# smallest_index = 0
#    for i in range(1,len(unvisited_queue)):
#       if unvisited_queue[1]
