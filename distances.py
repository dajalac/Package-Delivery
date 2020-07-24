# todo diescripitons
import csv

import csv

distance_list = []
vertices_minDistance_dic = {}
path_distance = []
path_vertices = []

with open('WGUPS_Distance_Table.csv', 'r') as csv_file:
    readCsv = csv.reader(csv_file, delimiter=',')
    print(readCsv)
    for row in readCsv:
        distance_list.append(row)


    def find_short_path(truck_addresses, got_to_hub, start_vertex=0):
        path_distance.clear()
        path_vertices.clear()
        global vertex
        minimum = 1000
        distance_accumulator = 0
        while len(truck_addresses) > 0:
            # print("initial vertex", start_vertex)
            for i in range(len(distance_list)):
                if distance_list[i][start_vertex] is '':
                    if 0 <= float(distance_list[start_vertex][i]) <= float(minimum):
                        if i in truck_addresses:
                            minimum = distance_list[start_vertex][i]
                            # print(" EMPTY in coluna  = %s and linha v %s with min distance of %s" % (
                            #      i, start_vertex, minimum))
                            vertex = i
                            min_distance = minimum
                            # start_vertex = i
                elif 0 <= float(distance_list[i][start_vertex]) <= float(minimum):
                    if i in truck_addresses:
                        minimum = distance_list[i][start_vertex]
                        # print(" in linha = %s and coluna =  %s with min distance of %s" % (i, start_vertex, minimum))
                        vertex = i
                        min_distance = minimum
                        # start_vertex = i
            ## esse block esta se reperinto a cada for loop
            vertices_minDistance_dic.update({vertex: minimum})
            path_distance.append(minimum)
            path_vertices.append(vertex)
            distance_accumulator += float(min_distance)
            # print("total acumulator", distance_accumulator)
            # print("final min distance", minimum)
            minimum = 100
            # print("vertex", vertex)
            # print("truck address list", truck_addresses)
            start_vertex = vertex
            t = truck_addresses.index(vertex)
            # print("############")
            current_vertex = truck_addresses.pop(t)
        if got_to_hub:
            # print("initial vertex", start_vertex)
            if distance_list[0][start_vertex] is '':
                min_distance = distance_list[start_vertex][0]
                distance_accumulator += float(min_distance)
                # print("total acumulator no final", distance_accumulator)
                # print(" EMPTY in coluna  = 0 and linha v %s with min distance of %s" % (start_vertex, min_distance))
                # print("distance from hub", min_distance)
            else:
                print("initial vertex", start_vertex)
                min_distance = distance_list[0][start_vertex]
                distance_accumulator += float(min_distance)
                # print("total acumulator no final", distance_accumulator)
                # print(" in linha = 0 and coluna =  %s with min distance of %s" % (start_vertex, min_distance))
                # print("distance from hub", min_distance)
            vertices_minDistance_dic.update({0: min_distance})
        print("dicionarion", vertices_minDistance_dic)
        print("vertices ,", path_vertices)
        print("distance,", path_distance)
        return vertex, distance_accumulator


    def get_shortPath():
        return path_distance, path_vertices
