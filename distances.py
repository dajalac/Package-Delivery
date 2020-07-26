# todo diescripitons
import csv

import csv

distance_list = []
path_distance = []
path_vertices = []

with open('WGUPS_Distance_Table.csv', 'r') as csv_file:
    readCsv = csv.reader(csv_file, delimiter=',')
    for row in readCsv:
        distance_list.append(row)

def find_short_path(truck_addresses):
        path_distance.clear()
        path_vertices.clear()
        start_vertex = 0
        global vertex
        minimum = 1000
        distance_accumulator = 0
        while len(truck_addresses) > 0:
            for i in range(len(distance_list)):
                if distance_list[i][start_vertex] is '':
                    if 0 <= float(distance_list[start_vertex][i]) <= float(minimum):
                        if i in truck_addresses:
                            minimum = distance_list[start_vertex][i]
                            vertex = i
                            min_distance = minimum
                elif 0 <= float(distance_list[i][start_vertex]) <= float(minimum):
                    if i in truck_addresses:
                        minimum = distance_list[i][start_vertex]
                        vertex = i
                        min_distance = minimum

            ## esse block esta se reperinto a cada for loop
            path_distance.append(minimum)
            path_vertices.append(vertex)
            distance_accumulator += float(min_distance)
            minimum = 1000
            start_vertex = vertex
            t = truck_addresses.index(vertex)
            current_vertex = truck_addresses.pop(t)
        if len(truck_addresses) == 0:
            if distance_list[0][start_vertex] is '':
                min_distance = distance_list[start_vertex][0]
                distance_accumulator += float(min_distance)
            else:
                min_distance = distance_list[0][start_vertex]
                distance_accumulator += float(min_distance)
        return distance_accumulator


def get_shortPath():
        return path_distance, path_vertices
