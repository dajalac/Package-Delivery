import csv

from package import Packages
from hashTable import MyHashTable
import readPackages

truck_one = []
truck_two = []
truck_three = []
hash_table = readPackages.get_hash_table()
MAX_LENGTH = 16


def load_trucks():
    print("Package #9 has the wrong address. It has to be corrected before it be out for delivery")
    # for i in range(1, hash_table.hash_length() + 1):
    #     item = hash_table.search(i)
    #     if item.package_deadline == "9:00 AM" and item.package_special_note == "":
    #         truck_one_priority.append(item)
    #     if item.package_deadline != "EOD" and "Must" in item.package_special_note:
    #         truck_one_EOB.append(item)
    #     elif item.package_deadline == "10:30 AM" and item.package_special_note == "":
    #         truck_one_EOB.append(item)
    #     elif item.package_id == 19:
    #         truck_one_EOB.append(item)
    #     elif "Wrong" in item.package_special_note:
    #         truck_three_EOB.append(item)
    #     elif item.package_deadline != "EOD" and "Delayed" in item.package_special_note:
    #         truck_two_priority.append(item)
    #     elif (len(truck_two_EOB) + len(truck_two_priority) + 1) < MAX_LENGTH:
    #         truck_two_EOB.append(item)
    #     else:
    #         truck_three_EOB.append(item)
    for i in [14, 15, 16, 34, 20, 21, 19, 1, 7, 29, 37, 30, 13, 39, 27, 35]:
        item = hash_table.search(i)
        truck_one.append(item)
        print("pag", item.package_id)
    for i in [25, 26, 22, 24, 28, 4, 40, 31, 32, 17, 6, 36, 12, 18, 23, 11]:
        item = hash_table.search(i)
        truck_two.append(item)
    for i in [2, 33, 10, 5, 38, 8, 9, 3]:
        item = hash_table.search(i)
        truck_three.append(item)


    print("Trucks loaded.")

    # # print("truck1 %s" % truck_one)
    # for i in truck_one_priority:
    #     print("truk1 PRIORITY id", i.package_id)
    # for i in truck_one_EOB:
    #     print("truk1 id", i.package_id)
    # # print("truck2 %s" % truck_two)
    # print("#########")
    # for i in truck_two_priority:
    #     print("truk2 PRIORITY id", i.package_id)
    # for i in truck_two_EOB:
    #     print("truk2 id", i.package_id)
    # print("#########")
    # # print("truck3 %s" % truck_three)
    # for i in truck_three_EOB:
    #     print("truk3 id", i.package_id)


def get_address_vertices():
    # get the address names
    with open("address.csv", 'r')as n:
        names = csv.reader(n, delimiter=',')
        names = list(names)

        address_vertices_dic = {}
        for i in range(len(names)):
            address_vertices_dic.update({names[i][1]: i}) # address = key and i = index (used to get the address vertex index


        vertices_address_dic = {}
        for i in range(len(names)):
            vertices_address_dic.update({i: names[i][1]}) # key = vertex and value = address
        return address_vertices_dic, vertices_address_dic


def get_vertices_truck1():
    address_dictionary,_ = get_address_vertices()
    truck1_vertices_EOB = []

    # get the address index for EOB packages
    for i in truck_one:
        truck1_vertices_EOB.append(address_dictionary[i.package_address])

    return list(set(truck1_vertices_EOB)) # remove duplicates


def get_vertices_truck2():
    address_dictionary,_ = get_address_vertices()
    truck2_vertices_EOB = []

    # get the address index for EOB packages
    for i in truck_two:
        truck2_vertices_EOB.append(address_dictionary[i.package_address])
    return list(set(truck2_vertices_EOB))#truck2_vertices_total


def get_vertices_truck3():
    address_dictionary,_ = get_address_vertices()
    truck3_vertices = []
    for i in truck_three:
        if i.package_id == 9:
            i.package_address = "410 S State St"
            i.package_zip = "84111"
            print("Package #9 address was corrected")
        truck3_vertices.append(address_dictionary[i.package_address])
    return list(set(truck3_vertices))




#b = load_trucks()
# a= get_vertices_truck1()
# b = get_vertices_truck2()
# c=get_vertices_truck3()