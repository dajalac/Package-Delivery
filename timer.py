import loadTruck
import readPackages

hash_table = readPackages.get_hash_table() # get the hash table

# this function will calculate the time based on the truck speed ( 18 miles per houres)
# it has the parameter mile. this is the total distance traveled by the truck until the address X
# Big O notation of O(1)
def time_per_mile(mile):
        minutes = (float(mile) * 60) / 18 # multiply by 60 to transform the the hour in minutes
        return minutes


# this function will determine what time each package was delivered
# It receives four parameters
# short_path_distance is the value calculated by the greedy algorithm.It holds the distances of the shortest path
# eg. [1.4, 3.5, 2.6]
# short_path_vertex is also calculated by the greedy algorithm. It holds the shortest path vertex
# e.g [0, 2, 34, 20]
# truck_number is regarding if the truck is the truck 1,2 or 3
# start_time is what time the truck will be out for deliverey.
# truck one will be out at 8:00
# truck two will be out at 9:10
# truck three will be out at 11:00
# Big O notation O(N^2)
def set_time(short_path_distance, short_path_vertex, truck_number, start_time):
        load_truck = loadTruck
        global packages_in_truck
        _, addresses_vertices = load_truck.get_address_vertices() #it will get the vertex-address dictionary e.g {0:hub}
        time = start_time

        # get the packages from truck
        if truck_number == 1:
            packages_in_truck = load_truck.get_truck_one_packages()
        elif truck_number == 2:
            packages_in_truck = load_truck.get_truck_two_packages()
        elif truck_number == 3:
            packages_in_truck = load_truck.get_truck_three_packages()

        # calculate time
        for i in range(len(short_path_distance)):
            # every loop iteration it will sum the the shortest distances
            # e.g short_path_distance [0.3, 2.4, 4.5]
            # the first interation 0 + 0.3 , so the fist package was delivered with 0.3 miles and the second with 0.3+2.4 ...
            # to convert to time, the miles accumulates will be send to time_per_mile function
            time += time_per_mile(short_path_distance[i])
            # to get the address name it will use the short_path_vertex and the vertex-address dictionary
            # so if the vertex is 0, the dictionary value for the key 0 is  = Hub
            selected_address = addresses_vertices[short_path_vertex[i]]

            # to set the delivery time for the package
            for package in packages_in_truck:
                # if the package in the truck has the same address as the current vertex of the shortest path it will
                # insert the calculated time as the time which the package as delivered
                if package.package_address == selected_address:
                    selected_package = hash_table.search(package.package_id)
                    selected_package.package_delivery = time

        return time # the total time will the used in the main to show what time each truck returned to the Hub




