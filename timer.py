import loadTruck
import readPackages
import datetime


def time_per_mile(mile):
    minutes = (float(mile)*60)/18
    return minutes

def set_time(short_path, truck_number, start_time, is_priority):

    addresses_vertices = loadTruck.get_address_vertices()
    time = start_time
    hash_table = readPackages.get_hash_table()
    # get the packages from truck
    if truck_number == 1 and is_priority:
        packages_in_truck = loadTruck.truck_one_priority
    elif truck_number==1 and is_priority == False:
        packages_in_truck= loadTruck.truck_one_EOB
    elif truck_number == 2 and is_priority:
        packages_in_truck = loadTruck.truck_two_priority
    elif truck_number == 2 and not is_priority:
        packages_in_truck = loadTruck.truck_two_EOB
    elif truck_number == 3: # Truck #3 has no packages with deadline priority
        packages_in_truck = loadTruck.truck_three_EOB

    # calculate time

    for i in short_path:
        time += time_per_mile(short_path[i])
        vertex = get_key(short_path[i],short_path)
        selected_address = get_key(vertex,addresses_vertices) if vertex is not None else None
        print("vertex", vertex, "and address ", selected_address)


        #to set the delivery time for the package
        for package in packages_in_truck:
            if package.package_address ==  selected_address:
                selected_package = hash_table.search(package.package_id)
                selected_package.delivery_status = "Delivered at:"+str(datetime.timedelta(minutes=time))
                print("pack id:", selected_package.package_id, " ", selected_package.delivery_status)
                print(" ")

    return time

# to retrieve keys for the dictionaries
def get_key(item, dictionary_list):
    for key, value in dictionary_list.items():
        if item == value:
            return key
    else:
        return None

