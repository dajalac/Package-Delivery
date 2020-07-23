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
    for i in range(1, hash_table.hash_length() + 1):
        item = hash_table.search(i)
        if item.package_deadline != "EOD" and "Must" in item.package_special_note:
            truck_one.append(item)
        elif item.package_deadline != "EOD" and item.package_special_note == "":
            truck_one.append(item)
        elif item.package_id == 19:
            truck_one.append(item)
        elif "Wrong" in item.package_special_note:
            truck_three.append(item)
        elif (item.package_deadline != "EOD" and "Delayed" in item.package_special_note) or len(truck_two) + 1 < MAX_LENGTH:
            truck_two.append(item)
        else:
            truck_three.append(item)
    print("Trucks loaded.")

    # print("truck1 %s" % truck_one)
    for i in truck_one:
        print("truk1 id", i.package_id)
    # print("truck2 %s" % truck_two)
    print("#########")
    for i in truck_two:
        print("truk2 id", i.package_id)
    print("#########")
    # print("truck3 %s" % truck_three)
    for i in truck_three:
        print("truk3 id", i.package_id)


def get_address_vertices():
    # get the address names
    with open("address.csv", 'r')as n:
        names = csv.reader(n, delimiter=',')
        names = list(names)

        address_vertices_dic = {}
        for i in range(len(names)):
            address_vertices_dic.update({names[i][1]: i})
        return address_vertices_dic


def get_vertices_truck1():
    address_dictionary = get_address_vertices()
    truck1_vertices = []

    for i in truck_one:
        truck1_vertices.append(address_dictionary[i.package_address])
    print("v for t1", truck1_vertices)
    return list(set(truck1_vertices)) # remove duplicates


def get_vertices_truck2():
    address_dictionary = get_address_vertices()
    truck2_vertices = []

    for i in truck_two:
        truck2_vertices.append(address_dictionary[i.package_address])
    print("v for t2", truck2_vertices)
    return list(set(truck2_vertices))


def get_vertices_truck3():
    address_dictionary = get_address_vertices()
    truck3_vertices = []
    for i in truck_three:
        if i.package_id == 9:
            i.package_address = "410 S State St"
            i.package_zip = "84111"
            print("Package #9 address was corrected")
        truck3_vertices.append(address_dictionary[i.package_address])
    print("v for t3", truck3_vertices)
    return list(set(truck3_vertices))


# b = load_trucks()
# a= get_vertices_truck1()
# b = get_vertices_truck2()
# c=get_vertices_truck3()