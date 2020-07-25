import datetime

from loadTruck import LoadTrucks
from distances import Distance
from timer import Timer
import lookUp
from lookUp import LookUp


def truck_out_for_delivery(package_address_vertices_list, truck_number, time):
    set_delivery = Timer()
    distances = Distance()
    travel_distance = distances.find_short_path(package_address_vertices_list)# !!!!! mudei p true
    shortPath_distance_list,shortPath_vertex_list = distances.get_shortPath()
    packages_time = set_delivery.set_time(shortPath_distance_list,shortPath_vertex_list, truck_number, time) #!!!! mudei p falso

    total_distance = travel_distance # + eob_distance
    total_time =packages_time # eob_packages_time
    #
    print("truck", truck_number, "total distance :", total_distance,"left at", str(datetime.timedelta(minutes=time)),
           "and returned at", str(datetime.timedelta(minutes=total_time)))



# load trucks

load_truck = LoadTrucks.load_trucks()

print("in main")
#truck 1

t1_address_vertices = load_truck.get_vertices_truck1()
truck_out_for_delivery(t1_address_vertices, 1, 8 * 60)
# truck 2
t2_address_vertices = load_truck.get_vertices_truck2()
truck_out_for_delivery(t2_address_vertices, 2, (9 * 60) + 10)

# truck 3
t3_address_vertices = load_truck.get_vertices_truck3()
truck_out_for_delivery(t3_address_vertices,3,(11*60))

# look up commands
print("Select from the following : ")
print(" 1 = Look up a package by its time ")
print(" 2 = Look up a package by ID")
print(" 3 = Show all packages")
print(" 4 = End the program ")

user_input = input()

mlist = load_truck.get_all_packages().copy()

look_up = LookUp()
look_up.lookUp_time(float(user_input*60),mlist)







