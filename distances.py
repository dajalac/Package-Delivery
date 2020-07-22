# todo diescripitons
import csv

import csv

distance_list = []
start_vertex = 0
with open('WGUPS_Distance_Table.csv', 'r') as csv_file:
    readCsv = csv.reader(csv_file, delimiter=',')
    print(readCsv)
    for row in readCsv:
        distance_list.append(row)

    def short_path(unvisited_queue):
       for unvisited_queue in distance_list:


    def short_path2(start_vertex):
        global vertx
        unvisited_queue = []
        for current_vertex in distance_list:
            unvisited_queue.append(current_vertex)

        min = 1000
        for i in range(len(unvisited_queue)):
            print("i", i)
            if distance_list[i][start_vertex] is '':  # here I think that we should use unvisited-quee
                if 0 < float(distance_list[start_vertex][i]) <= float(min):
                    min = distance_list[start_vertex][i]
                    print("mindistance", min)
                    vertx = i
            elif 0 < float(distance_list[i][start_vertex]) <= float(min):
                min = distance_list[i][start_vertex]
                print("min distance 3", min)
                vertx = i

        print("vertexi", vertx)
        current_vertex = unvisited_queue.pop(vertx)
        print((current_vertex))
        # start_vertex= vertx
        print(current_vertex)

        # I should use unvisited_quere instead of distance_list
        # start_vertex should be 0 and change vertex (lugar onde parou com a minima distance).
        #p cada current vertex criar um module que add q foi entregue e a hora.

