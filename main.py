import datetime

import loadTruck
import distances
from timer import set_time


def truck_out_for_delivery(priority_vertices_list, eob_vertices_list, truck_number, time):
    #  for packages with priority delivery time

    priority_endPoint, priority_distance = distances.find_short_path(priority_vertices_list, got_to_hub=False)
    priority_shortPath_distance,priority_shortPath_vertex = distances.get_shortPath()
    priority_packages_time = set_time(priority_shortPath_distance,priority_shortPath_vertex, truck_number, time, is_priority=True)
    #
    # # for packages with EOD deadline
    _, eob_distance = distances.find_short_path(eob_vertices_list, True,
                                                           priority_endPoint)  # true = go_to_hub
    eob_shortPath_distance, eob_shortPath_vertex = distances.get_shortPath()
    eob_packages_time = set_time(eob_shortPath_distance, eob_shortPath_vertex, truck_number, priority_packages_time, is_priority=False)
    #
    total_distance = priority_distance + eob_distance
    total_time = eob_packages_time
    #
    print("truck", truck_number, "total distance :", total_distance,"left at", str(datetime.timedelta(minutes=time)),
           "and returned at", str(datetime.timedelta(minutes=total_time)))



# load trucks
load_truck = loadTruck.load_trucks()

#truck 1
# get trucks address list - in vertices
t1_address_vertices_EOB = loadTruck.get_vertices_truck1()[1]
t1_address_vertices_priority= loadTruck.get_vertices_truck1()[0]
# to sent truck out for delivery
truck_out_for_delivery(t1_address_vertices_priority,t1_address_vertices_EOB,1,8*60)

# truck 2
t2_address_vertices_EOB = loadTruck.get_vertices_truck2()[1]
t2_address_vertices_priority = loadTruck.get_vertices_truck2()[0]
# to sent truck out for delivery
truck_out_for_delivery(t2_address_vertices_priority,t2_address_vertices_EOB,2,(9*60)+10)

#truck 3
t3_address_vertices = loadTruck.get_vertices_truck3()
t3_priority=[0] # it has no priority packages
truck_out_for_delivery(t3_priority,t3_address_vertices,3,(11*60))





