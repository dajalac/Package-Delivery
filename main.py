import loadTruck
from  distances import short_path

# load trucks

load_truck = loadTruck.load_trucks()

# get trucks address list - in vertices
t1_address_vertices = loadTruck.get_vertices_truck1()
print("t1 vertix adress in main", t1_address_vertices)

t2_address_vertices = loadTruck.get_vertices_truck2()
print("t2 vertixe in main", t2_address_vertices)

# if time is 10:35 correct address

t3_address_vertices = loadTruck.get_vertices_truck3()
print("t3 vertixe in main", t3_address_vertices)

## if time = 8: truck 1 is out

distance = short_path(t1_address_vertices)

## if time = 9:10 truck 2

## when truck 1 return, truck 3 is out




