import datetime

import loadTruck
#from distances import Distance
import distances
#from timer import Timer
import timer
import lookUp
#from lookUp import LookUp



def truck_out_for_delivery(package_address_vertices_list, truck_number, time):
    travel_distance = distances.find_short_path(package_address_vertices_list)  # !!!!! mudei p true
    shortPath_distance_list, shortPath_vertex_list = distances.get_shortPath()
    packages_time = timer.set_time(shortPath_distance_list, shortPath_vertex_list, truck_number,
                                       time)  # !!!! mudei p falso


    total_time = packages_time  # eob_packages_time
    print("----------------------------------------------------------------------------")
    print("Truck", truck_number, "traveled ", round(travel_distance,2),"miles, Left at",
              str(datetime.timedelta(minutes=time)),
              "and returned at", str(datetime.timedelta(minutes=packages_time)))

 # load trucks
load_truck = loadTruck.load_trucks()

    # truck 1

t1_address_vertices = loadTruck.get_vertices_truck1()
truck_out_for_delivery(t1_address_vertices, 1, 8 * 60)
    # truck 2
t2_address_vertices = loadTruck.get_vertices_truck2()
truck_out_for_delivery(t2_address_vertices, 2, (9 * 60) + 10)

    # truck 3
t3_address_vertices = loadTruck.get_vertices_truck3()
truck_out_for_delivery(t3_address_vertices, 3, (11 * 60))

##


    # look up commands
print(" ")
print("Select from the following : ")
print(" 1 = Look up a package by its time ")
print(" 2 = Look up a package by ID")
print(" 3 = Show all packages")
print(" 4 = End the program ")

user_input = input()

if user_input == "1":
    error = True
    while error :
        print("Enter a time :")
        print("Note: time must be 24h format HH:MM")
        print("Example: 16:00")
        hour_input = input()
        try:
            ## treat imput 1
            (h,m) = hour_input.split(':')
            time_formated = float(h)*60+float(m)
            error =False
            lookUp.lookUp_time(time_formated)
        except:
            print("Please review your input and try again")
            error = True
            pass


if user_input == "2":
    error = True
    while error:
        print("Enter a package ID : ")
        pack_id = input()
        try:
            error: False
            lookUp.luckUp_id(int(pack_id))
        except:
            print("Please review your input and try again")
            error = True
            pass

if user_input == "3":
    lookUp.lookUp_time(float(15* 60))
if user_input == "4":
    exit()

    # look_up = lookUp
# def truck_out_for_delivery(package_address_vertices_list, truck_number, time):
#
#
#     travel_distance = distances.find_short_path(package_address_vertices_list)# !!!!! mudei p true
#     shortPath_distance_list,shortPath_vertex_list = distances.get_shortPath()
#     packages_time = timer.set_time(shortPath_distance_list,shortPath_vertex_list, truck_number, time) #!!!! mudei p falso
#
#     total_distance = travel_distance # + eob_distance
#     total_time =packages_time # eob_packages_time
#     #
#     print("truck", truck_number, "total distance :", total_distance,"left at", str(datetime.timedelta(minutes=time)),
#            "and returned at", str(datetime.timedelta(minutes=total_time)))
#
#
#  # load trucks
# load_truck = loadTruck.load_trucks()
#
# print("in main")
#     # truck 1
#
# t1_address_vertices = loadTruck.get_vertices_truck1()
# truck_out_for_delivery(t1_address_vertices, 1, 8 * 60)
#     # truck 2
# t2_address_vertices = loadTruck.get_vertices_truck2()
# truck_out_for_delivery(t2_address_vertices, 2, (9 * 60) + 10)
#
#     # truck 3
# t3_address_vertices = loadTruck.get_vertices_truck3()
# truck_out_for_delivery(t3_address_vertices, 3, (11 * 60))
#
#     # look up commands
# print("Select from the following : ")
# print(" 1 = Look up a package by its time ")
# print(" 2 = Look up a package by ID")
# print(" 3 = Show all packages")
# print(" 4 = End the program ")
#
# user_input = input()
#
# lookUp.lookUp_time(float(int(user_input) * 60))
#
#     # look_up = lookUp

