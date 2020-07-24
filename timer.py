import loadTruck
import readPackages
import datetime


def time_per_mile(mile):
    minutes = (float(mile)*60)/18
    return minutes

def set_time(short_path_distance,short_path_vertex, truck_number, start_time):
    print("start time", str(datetime.timedelta(minutes=start_time)))
    _,addresses_vertices = loadTruck.get_address_vertices()
    time = start_time
    hash_table = readPackages.get_hash_table()
    # get the packages from truck

    if truck_number==1:
        packages_in_truck= loadTruck.truck_one
    elif truck_number == 2:
        packages_in_truck = loadTruck.truck_two
    elif truck_number == 3: # Truck #3 has no packages with deadline priority
        packages_in_truck = loadTruck.truck_three

    # calculate time

    for i in range(len(short_path_distance)):

        # print("vertice current",short_path[i])
        print("value to add in time",str(datetime.timedelta(minutes=time_per_mile(short_path_distance[i]))))
        print("current vertex",short_path_vertex[i])
        print("current distance",short_path_distance[i])
        print("time antes de somado", str(datetime.timedelta(minutes=time)))
        time += time_per_mile(short_path_distance[i])
        selected_address = addresses_vertices[short_path_vertex[i]]
        print("time depois de somado", str(datetime.timedelta(minutes=time)))
        print ("current address", selected_address)

        #to set the delivery time for the package
        for package in packages_in_truck:
            if package.package_address ==  selected_address:
                selected_package = hash_table.search(package.package_id)
                selected_package.delivery_status = "Delivered at:"+str(datetime.timedelta(minutes=time))
                print("pack id:", selected_package.package_id, " ", selected_package.delivery_status)
                print(" ")
    print("total time nessa rodada",str(datetime.timedelta(minutes=time)))

    return time


