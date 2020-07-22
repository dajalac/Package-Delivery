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

    # # tira os ' ' = acho q n vou usar
    # distance = []
    # for row in distance_list:
    #     c = [i for i in row if i != '']
    #     distance.append(c)
    # print(distance)

    s = [2,3,4,7,19]
    min = 1000
    adistance_acumulator = 0
    while len(s) > 0:
        print("initial vertex", start_vertex)

        for i in range(len(unvisited_queue)):
            if unvisited_queue[i][start_vertex] is '':  # here I think that we should use unvisited-quee
                if 0 < float(unvisited_queue[start_vertex][i]) <= float(min):
                    if i in s:
                        min = unvisited_queue[start_vertex][i]
                        print(" EMPTY in coluna  = %s and linha v %s with min distance of %s" % (i, start_vertex, min))
                        vertx = i
                        min_distance = min
                        #start_vertex = i
            elif 0 < float(unvisited_queue[i][start_vertex]) <= float(min):
                if i in s:
                    min = unvisited_queue[i][start_vertex]
                    print(" in linha = %s and coluna =  %s with min distance of %s" %(i,start_vertex,min))
                    vertx = i
                    min_distance = min
                    #start_vertex = i
        ## esse block esta se reperinto a cada for loop
        adistance_acumulator += float(min_distance)
        print("total acumulator", adistance_acumulator)
        print("final min distance", min)
        min = 100
        print("vertex", vertx)
        print("s list", s)
        start_vertex = vertx
        t = s.index(vertx)
        print("############")
        current_vertex = s.pop(t)
    if len(s) == 0:
        print("initial vertex", start_vertex)
        if unvisited_queue[0][start_vertex] is '':
            min = unvisited_queue[start_vertex][0]
            adistance_acumulator += float(min_distance)
            print("total acumulator", adistance_acumulator)
            print(" EMPTY in coluna  = 0 and linha v %s with min distance of %s" % (start_vertex, min))
            print("distance from hub", min)
        else:
            print("initial vertex", start_vertex)
            min = unvisited_queue[0][start_vertex]
            adistance_acumulator += float(min_distance)
            print("total acumulator", adistance_acumulator)
            print(" in linha = 0 and coluna =  %s with min distance of %s" % (start_vertex, min))
            print("distance from hub", min)





a = dj(0)

# start_vertex_distance = distance_list[start_vertex][start_vertex]


# while len(unvisited_queue) >0 :
# smallest_index = 0
#    for i in range(1,len(unvisited_queue)):
#       if unvisited_queue[1]
