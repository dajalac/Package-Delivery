# Danielle Ajala Cruz 001179605
import datetime
import loadTruck
import distances
import timer
import lookUp
import sys


# this function will sent the trucks out for delivery
# it will first calculate the shortest path which the truck must travel in order to delivery all packages on time
# to do this it will use the find_short_path function (the greedy algorithm)
# you can find the find_short_path and get_shortPath on distance.py
# after get the shortest path, this function will use the set_time function, which will be used to set the delivery
# time for all packages. You can find the set_time function on timer.py
# Big O notation of O(N^2) because both find_short_path and set_time are O(N^2)
def truck_out_for_delivery(package_address_vertices_list, truck_number, time):
    travel_distance = distances.find_short_path(package_address_vertices_list)
    shortPath_distance_list, shortPath_vertex_list = distances.get_shortPath()
    packages_time = timer.set_time(shortPath_distance_list, shortPath_vertex_list, truck_number, time)

    print("----------------------------------------------------------------------------")
    print("Truck", truck_number, "traveled ", round(travel_distance, 2), "miles, Left at",
          str(datetime.timedelta(minutes=time)),
          "and returned at", str(datetime.timedelta(minutes=packages_time)))


# load trucks
load_truck = loadTruck.load_trucks()

# truck 1
# it will call the truck_out_for_delivery function
# the arguments are:
# t1_address_vertices which are the address index of each package on the truck one
# the t1_address_vertices ware calculated at loadTruck.py
# 1 represent the truck number
# 8 represents what time the truck 1 left for delivery. It is multiplies by 60 to transforms hours to minutes
t1_address_vertices = loadTruck.get_vertices_truck1()
truck_out_for_delivery(t1_address_vertices, 1, 8 * 60)

# truck 2
# it does the same as the statements above, but for the truck two
# 2 represents the truck number
#  the truck 2 left at 9:10 AM, the (9*60 + 10) is used to transform hours in minutes
t2_address_vertices = loadTruck.get_vertices_truck2()
truck_out_for_delivery(t2_address_vertices, 2, (9 * 60) + 10)

# truck 3
# the truck 3 left at 11:00 AM
t3_address_vertices = loadTruck.get_vertices_truck3()
truck_out_for_delivery(t3_address_vertices, 3, (11 * 60))

# the user interface
# look up commands
print(" ")
print("Select from the following : ")
print(" 1 = Look up a package by its time ")
print(" 2 = Look up a package by ID")
print(" 3 = Show all packages")
print(" 4 = End the program ")

user_input = input()  # holds the user input

# It will show the the packages delivery status according to the user time input
# Big O notation of O(n)
if user_input == "1":
    error = True
    while error:  # it will replay this message if the user insert a illegal input
        print("Enter a time :")
        print("Note: time must be 24h format HH:MM")
        print("Example: 16:00")
        hour_input = input()
        try:
            # treat imput 1
            (h, m) = hour_input.split(':')
            time_formated = float(h) * 60 + float(m)  # transform hours to minutes
            error = False
            lookUp.lookUp_time(time_formated)
        except:
            print("Please review your input and try again")
            error = True
            pass

# it will show the package that the user chooses
# Big O of O(n)
if user_input == "2":
    print("Enter a package ID : ")
    pack_id = input()
    try:
        input_id = pack_id
        error: False
        lookUp.lookUp_id(int(input_id))
    except:
        print("Please review your input and try again")
        import subprocess
        subprocess.call("main.py", shell=True)

# if user_input == "2":
#     error = True
#     while error:
#         print("Enter a package ID : ")
#         pack_id = input()
#         try:
#             input_id = pack_id
#             error: False
#             lookUp.lookUp_id(int(input_id))
#         except:
#             print("Please review your input and try again")
#             error = True
#             pass

# show the delivery time for all packages
# Big O notation of O(N)
if user_input == "3":
    lookUp.lookUp_time(float(15 * 60))

# exit the program
# Big O notation of O(1)
if user_input == "4":
    sys.exit()
