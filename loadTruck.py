import csv

from package import Packages
from hashTable import MyHashTable
import readPackages

truck_one = []
truck_two = []
truck_three = []
hash_table = readPackages.get_hash_table()
MAX_LENGTH = 16

for i in range(1, hash_table.hash_length() + 1):
    print("###########len truck 2", len(truck_two))
    item = hash_table.search(i)
    if item.package_deadline != "EOD" and "Must" in item.package_special_note:
        truck_one.append(item)
    elif item.package_deadline != "EOD" and item.package_special_note == "":
        truck_one.append(item)
    elif item.package_id == 19:
        truck_one.append(item)
    elif (item.package_deadline != "EOD" and "Delayed" in item.package_special_note) or len(truck_two) + 1 < MAX_LENGTH:
        truck_two.append(item)
    else:
        truck_three.append(item)

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


a= get_address_vertices()