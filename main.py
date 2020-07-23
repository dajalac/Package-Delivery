import loadTruck
from  distances import *

# load trucks

load_truck = loadTruck.load_trucks()

# get trucks address list - in vertices
t1_address_vertices_EOB = loadTruck.get_vertices_truck1()[1]
t1_address_vertices_priority= loadTruck.get_vertices_truck1()[0]

print("t1 vertix adress in main", t1_address_vertices_EOB)

t2_address_vertices_EOB = loadTruck.get_vertices_truck2()[1]
t2_address_vertices_priority = loadTruck.get_vertices_truck2()[0]
print("t2 vertixe in main", t2_address_vertices_EOB)
#
# # if time is 10:35 correct address
#
t3_address_vertices = loadTruck.get_vertices_truck3()
print("t3 vertixe in main", t3_address_vertices)

## if time = 8: truck 1 is out

#t1_priority= short_path2(t1_address_vertices_priority,False)
find_short_path(t1_address_vertices_EOB,True,21)

## if time = 9:10 truck 2
#distance2 = short_path(t2_address_vertices)

## when truck 1 return, truck 3 is out
#distance3 = short_path(t3_address_vertices)




