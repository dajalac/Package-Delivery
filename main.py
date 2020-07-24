import datetime

import loadTruck
import distances
from timer import set_time

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
# priority
t1_priority_endPoint, distances_priority = distances.find_short_path(t1_address_vertices_priority, False)
t1_priority_short_path = distances.get_shortPath()
print("total distance p o t1", distances_priority)
t1_priority_time = set_time(t1_priority_short_path,1,8*60,True)
print("start delivery time p o eob", t1_priority_time)
# # eob pachakes
t1_EOD_endPoint, distances_EOD = distances.find_short_path(t1_address_vertices_EOB, t1_priority_endPoint, True)
t1_EOB_short_path = distances.get_shortPath()
t1_EOB_time = set_time(t1_EOB_short_path,1, t1_priority_time,False)
#
print("truck one left at 8 AM and returned at ",str(datetime.timedelta(minutes=(t1_EOB_time))))
print("truck one traveled ", distances_priority+distances_EOD)

#find_short_path(t1_address_vertices_EOB,True,21)


## if time = 9:10 truck 2
#distance2 = short_path(t2_address_vertices)

## when truck 1 return, truck 3 is out
#distance3 = short_path(t3_address_vertices)




