#from loadTruck import LoadTrucks
import loadTruck
import readPackages
import datetime
import lookUp

hash_table = readPackages.get_hash_table()


def time_per_mile(mile):
        minutes = (float(mile) * 60) / 18
        return minutes


def set_time(short_path_distance, short_path_vertex, truck_number, start_time):
        load_truck = loadTruck
        #global packages_in_truck
        global packages_in_truck
        #print("start time", str(datetime.timedelta(minutes=start_time)))
        _, addresses_vertices = load_truck.get_address_vertices()
        time = start_time

        # get the packages from truck
        if truck_number == 1:
            packages_in_truck = load_truck.get_truck_one_packages()
            # change to load status
            #change_status(loadTruck.get_truck_one_packages())
        elif truck_number == 2:
            packages_in_truck = load_truck.get_truck_two_packages()

            #change_status(packages_in_truck)
        elif truck_number == 3:  # Truck #3 has no packages with deadline priority
            packages_in_truck = load_truck.get_truck_three_packages()
            #change_status(packages_in_truck)

        # calculate time

        for i in range(len(short_path_distance)):

            # print("vertice current",short_path[i])
            # print("value to add in time", str(datetime.timedelta(minutes= time_per_mile(short_path_distance[i]))))
            # print("current vertex", short_path_vertex[i])
            # print("current distance", short_path_distance[i])
            # print("time antes de somado", str(datetime.timedelta(minutes=time)))
            time += time_per_mile(short_path_distance[i])
            #print("time sem transformar", time)
            selected_address = addresses_vertices[short_path_vertex[i]]
            # print("time depois de somado", str(datetime.timedelta(minutes=time)))
            # print("current address", selected_address)

            # to set the delivery time for the package
            for package in packages_in_truck:
                if package.package_address == selected_address:
                    selected_package = hash_table.search(package.package_id)
                    # mudei, como vai ser display na copy só uma os minutos brutos
                    #selected_package.package_delivery = "Delivered at:" + str(datetime.timedelta(minutes=time))
                    selected_package.package_delivery = time
                    # print("pack id hehe:", selected_package.package_id, " delivered at ", str(datetime.timedelta(minutes=time)))
                    # print(" ")


            # if time == 541.3333333333335:  # 9:01:20
            #     take_screen_shot()
        # if time == 604.6666666666669 : #10:04:40
        #     take_screen_shot(time)
        # if time == 729.0000000000001: # 12:09:00
        #     take_screen_shot(time)

        #print("total time nessa rodada", str(datetime.timedelta(minutes=time)))

        return time


    # tb NAO precisa disso, pq isso sera colocado na copia
# def change_status(packages_list):
#         # hash_table = readPackages.get_hash_table()
#         for i in packages_list:
#             item = hash_table.search(i.package_id)
#             item.package_delivery= "Out for delivery"

# class Timer:
#     def time_per_mile(self,mile):
#         minutes = (float(mile) * 60) / 18
#         return minutes
#
#
#     def set_time(self,short_path_distance, short_path_vertex, truck_number, start_time):
#         load_truck = LoadTrucks()
#         #global packages_in_truck
#         global packages_in_truck
#         print("start time", str(datetime.timedelta(minutes=start_time)))
#         _, addresses_vertices = load_truck.get_address_vertices()
#         time = start_time
#
#         # get the packages from truck
#         if truck_number == 1:
#             packages_in_truck = load_truck.get_truck_one_packages()
#             # change to load status
#             #change_status(loadTruck.get_truck_one_packages())
#         elif truck_number == 2:
#             packages_in_truck = load_truck.get_truck_two_packages()
#
#             #change_status(packages_in_truck)
#         elif truck_number == 3:  # Truck #3 has no packages with deadline priority
#             packages_in_truck = load_truck.get_truck_three_packages()
#             #change_status(packages_in_truck)
#
#         # calculate time
#
#         for i in range(len(short_path_distance)):
#
#             # print("vertice current",short_path[i])
#             print("value to add in time", str(datetime.timedelta(minutes=self.time_per_mile(short_path_distance[i]))))
#             print("current vertex", short_path_vertex[i])
#             print("current distance", short_path_distance[i])
#             print("time antes de somado", str(datetime.timedelta(minutes=time)))
#             time += self.time_per_mile(short_path_distance[i])
#             print("time sem transformar", time)
#             selected_address = addresses_vertices[short_path_vertex[i]]
#             print("time depois de somado", str(datetime.timedelta(minutes=time)))
#             print("current address", selected_address)
#
#             # to set the delivery time for the package
#             for package in packages_in_truck:
#                 if package.package_address == selected_address:
#                     selected_package = hash_table.search(package.package_id)
#                     # mudei, como vai ser display na copy só uma os minutos brutos
#                     #selected_package.package_delivery = "Delivered at:" + str(datetime.timedelta(minutes=time))
#                     selected_package.package_delivery = time
#                     print("pack id hehe:", selected_package.package_id, " delivered at ", str(datetime.timedelta(minutes=time)))
#                     print(" ")
#
#
#             # if time == 541.3333333333335:  # 9:01:20
#             #     take_screen_shot()
#         # if time == 604.6666666666669 : #10:04:40
#         #     take_screen_shot(time)
#         # if time == 729.0000000000001: # 12:09:00
#         #     take_screen_shot(time)
#
#         print("total time nessa rodada", str(datetime.timedelta(minutes=time)))
#
#         return time
#
#
#     # tb NAO precisa disso, pq isso sera colocado na copia
#     def change_status(self,packages_list):
#         # hash_table = readPackages.get_hash_table()
#         for i in packages_list:
#             item = hash_table.search(i.package_id)
#             item.package_delivery= "Out for delivery"


