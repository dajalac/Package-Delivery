# todo diescripitons
import csv

import csv

distance_list = []


with open('WGUPS_Distance_Table.csv', 'r') as csv_file:
    readCsv = csv.reader(csv_file, delimiter=',')
    print(readCsv)
    for row in readCsv:
        distance_list.append(row)

    def short_path(truck_addresses):
        start_vertex = 0
        global vertex
        minimum = 1000
        distance_accumulator = 0
        while len(truck_addresses) > 0:
            print("initial vertex", start_vertex)
            for i in range(len(distance_list)):
                if distance_list[i][start_vertex] is '':
                    if 0 < float(distance_list[start_vertex][i]) <= float(minimum):
                        if i in truck_addresses:
                            minimum = distance_list[start_vertex][i]
                            print(" EMPTY in coluna  = %s and linha v %s with min distance of %s" % (
                                i, start_vertex, minimum))
                            vertex = i
                            min_distance = minimum
                            # start_vertex = i
                elif 0 < float(distance_list[i][start_vertex]) <= float(minimum):
                    if i in truck_addresses:
                        minimum = distance_list[i][start_vertex]
                        print(" in linha = %s and coluna =  %s with min distance of %s" % (i, start_vertex, minimum))
                        vertex = i
                        min_distance = minimum
                        # start_vertex = i
            ## esse block esta se reperinto a cada for loop
            distance_accumulator += float(min_distance)
            print("total acumulator", distance_accumulator)
            print("final min distance", minimum)
            minimum = 100
            print("vertex", vertex)
            print("s list", truck_addresses)
            start_vertex = vertex
            t = truck_addresses.index(vertex)
            print("############")
            current_vertex = truck_addresses.pop(t)
        if len(truck_addresses) == 0:
            print("initial vertex", start_vertex)
            if distance_list[0][start_vertex] is '':
                minimum = distance_list[start_vertex][0]
                distance_accumulator += float(min_distance)
                print("total acumulator", distance_accumulator)
                print(" EMPTY in coluna  = 0 and linha v %s with min distance of %s" % (start_vertex, minimum))
                print("distance from hub", minimum)
            else:
                print("initial vertex", start_vertex)
                minimum = distance_list[0][start_vertex]
                distance_accumulator += float(min_distance)
                print("total acumulator", distance_accumulator)
                print(" in linha = 0 and coluna =  %s with min distance of %s" % (start_vertex, minimum))
                print("distance from hub", minimum)



    def short_path2(start_vertex):
        global vertex
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
                    vertex = i
            elif 0 < float(distance_list[i][start_vertex]) <= float(min):
                min = distance_list[i][start_vertex]
                print("min distance 3", min)
                vertex = i

        print("vertexi", vertex)
        current_vertex = unvisited_queue.pop(vertex)
        print((current_vertex))
        # start_vertex= vertx
        print(current_vertex)

        # I should use unvisited_quere instead of distance_list
        # start_vertex should be 0 and change vertex (lugar onde parou com a minima distance).
        #p cada current vertex criar um module que add q foi entregue e a hora.

