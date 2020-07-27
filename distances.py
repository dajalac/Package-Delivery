import csv

distance_list = []  # holds the values from WGUPS_Distance_table.cvs
path_distance = []  # holds the shortest path distances values
path_vertices = []  # holds the shortest path addresses vertices

# it will open the WGUPS_Distance_table.cvs and save it in the distance_list adjacency list
# Big O notation of O(n)
with open('WGUPS_Distance_Table.csv', 'r') as csv_file:
    readCsv = csv.reader(csv_file, delimiter=',')
    for row in readCsv:
        distance_list.append(row)  # appends each row of the distance matrix in a adjacency list


# This is my greedy algorithm
# it will calculate the shortest path that a truck must travel in oder to delivery all the packages on time
# Big O notation of O(N^2)
def find_short_path(truck_addresses):
    path_distance.clear()  # every time the function is called I have to clean the path_distance list
    path_vertices.clear()  # every time the function is called I have to clean the path_vertices list
    start_vertex = 0  # for the fist loop interaction the truck must departure from the hub (vertex index = 0)
    global vertex
    minimum_distance = 1000  # it can be initialized to any value bigger the the biggest value of the distance matrix
    # I choose 1000 in case in the future the matrix be implemented with more values
    distance_accumulator = 0

    while len(truck_addresses) > 0:
        for i in range(len(distance_list)):
            # in case the value is empty, I switched the columns and lines. It is necessary because the distance matrix
            # is a type of similarity matrix, i.e it is just a "half" matrix because one side is the copy of the other.
            if distance_list[i][start_vertex] is '':
                if 0 <= float(distance_list[start_vertex][i]) <= float(minimum_distance):
                    # the shortest distance will only be picked if the address selected is the destination of one of
                    # the packages in the truck, otherwise the loop will continue to the next address
                    if i in truck_addresses:
                        minimum_distance = distance_list[start_vertex][i]
                        vertex = i  # it will be the next start address instead of the hub
            # this will do the same thing as the if statement, but in chase the cell selected is not empty
            elif 0 <= float(distance_list[i][start_vertex]) <= float(minimum_distance):
                if i in truck_addresses:
                    minimum_distance = distance_list[i][start_vertex]
                    vertex = i

        # the path_distance and path_vertices will be uses in timer.py to calculate the delivery time of the packages
        path_distance.append(minimum_distance)
        path_vertices.append(vertex)
        distance_accumulator += float(minimum_distance)
        minimum_distance = 1000
        start_vertex = vertex
        t = truck_addresses.index(vertex)
        current_vertex = truck_addresses.pop(t)  # remove the current address from the truck address list to
        # avoid the same address to be visited twice

    # when the truck address list is empty (when all the packages were delivered) the truck must return to the hub
    if len(truck_addresses) == 0:
        # here I also included a statement to check if the current cell is empty.
        if distance_list[0][start_vertex] is '':
            min_distance = distance_list[start_vertex][0]
            distance_accumulator += float(min_distance)
        else:
            min_distance = distance_list[0][start_vertex]
            distance_accumulator += float(min_distance)
    return distance_accumulator  # I choose to return the total distance traveled, but you can return path_distance and
    # or path_vertices as well.


# this function will return the path_distance and path_vertices. They will be used to calculate the delivery time
# Big O notation of O(1)
def get_shortPath():
    return path_distance, path_vertices
