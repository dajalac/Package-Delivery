import datetime

import loadTruck
import distances
from timer import set_time

#def truck_out_for_delivery(priority_vertices_list, eob_vertices_list, truck_number, time):
def truck_out_for_delivery(package_address_vertices_list, truck_number, time):

    #  for packages with priority delivery time
    print("priority vertices", package_address_vertices_list)
    travel_distance = distances.find_short_path(package_address_vertices_list)# !!!!! mudei p true
    shortPath_distance_list,shortPath_vertex_list = distances.get_shortPath()
    packages_time = set_time(shortPath_distance_list,shortPath_vertex_list, truck_number, time) #!!!! mudei p falso
    #
    # # for packages with EOD deadline
    # _, eob_distance = distances.find_short_path(eob_vertices_list, True,
    #                                                        priority_endPoint)  # true = go_to_hub
    # eob_shortPath_distance, eob_shortPath_vertex = distances.get_shortPath()
    # eob_packages_time = set_time(eob_shortPath_distance, eob_shortPath_vertex, truck_number, priority_packages_time, is_priority=False)
    #
    total_distance = travel_distance # + eob_distance
    total_time =packages_time # eob_packages_time
    #
    print("truck", truck_number, "total distance :", total_distance,"left at", str(datetime.timedelta(minutes=time)),
           "and returned at", str(datetime.timedelta(minutes=total_time)))



# load trucks
load_truck = loadTruck.load_trucks()

#truck 1
# get trucks address list - in vertices
# t1_address_vertices_EOB = loadTruck.get_vertices_truck1()[1]
# t1_address_vertices_priority= loadTruck.get_vertices_truck1()[0]
t1_address_vertices = loadTruck.get_vertices_truck1()
# to sent truck out for delivery
truck_out_for_delivery(t1_address_vertices, 1, 8 * 60)
#truck_out_for_delivery(t1_address_vertices_priority,t1_address_vertices_EOB,1,8*60)

# truck 2
# t2_address_vertices_EOB = loadTruck.get_vertices_truck2()[1]
# t2_address_vertices_priority = loadTruck.get_vertices_truck2()[0]
t2_address_vertices = loadTruck.get_vertices_truck2()
# to sent truck out for delivery
truck_out_for_delivery(t2_address_vertices, 2, (9 * 60) + 10)
#truck_out_for_delivery(t2_address_vertices_priority,t2_address_vertices_EOB,2,(9*60)+10)

#truck 3
t3_address_vertices = loadTruck.get_vertices_truck3()
#t3_priority=[0] # it has no priority packages
truck_out_for_delivery(t3_address_vertices,3,(11*60))





