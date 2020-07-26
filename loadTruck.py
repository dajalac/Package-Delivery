import csv
import readPackages

truck_one = []  # hold packages for truck one
truck_two = []  # hold packages for truck two
truck_three = []  # hold packages for truck three
all_package = []  # hold all packages
hash_table = readPackages.get_hash_table()
MAX_LENGTH = 16  # maximum amount of packages on truck


# this function will load the packages in the truck
# the number list represents the packages Id
# on each loop interaction the package Id will be used to search for the package object in the hash table
# after the hash table return the package desired it will be insert on the designed truck list
# Big O notation of O(1) because even though it has for loop, the amount of loop interaction will be constant
def load_trucks():
    for i in [14, 15, 16, 34, 20, 21, 19, 1, 7, 29, 37, 30, 13, 39, 27, 35]:
        item = hash_table.search(i)
        truck_one.append(item)
    for i in [25, 26, 22, 24, 28, 4, 40, 31, 32, 17, 6, 36, 12, 18, 38, 3]:
        item = hash_table.search(i)
        truck_two.append(item)
    for i in [2, 33, 10, 5, 23, 8, 9, 11]:
        item = hash_table.search(i)
        truck_three.append(item)
    for i in range(1, 41):
        item = hash_table.search(i)
        all_package.append(item)


# I saved the addresses in another csv file
# this function will read the address file and save it in the name list
# after read the csv file, the function will insert the addresses in a dictionary
# I created two dictionaries, address-vertices and vertices-address
# the address-vertices will be used to associate the distance matrix with the addresses (to make easier,
# I removed the addresses of the distance matrix and use its indexes instead). It is uses in distance.py
# the vertices-address will be used to convert the vertices back to addresses and will be used in the timer.py
# Big O notation of O(n)
def get_address_vertices():
    # get the address names
    with open("address.csv", 'r')as n:
        names = csv.reader(n, delimiter=',')
        names = list(names)

        address_vertices_dic = {}  # initialize the dictionary addresses - vertices
        for i in range(len(names)):
            address_vertices_dic.update(
                {names[i][1]: i})  # address = key and i = value e.g  {Hub : 0}

        vertices_address_dic = {}  # initialize the dictionary vertices - addresses
        for i in range(len(names)):
            vertices_address_dic.update({i: names[i][1]})  # key = vertex and value = address {0: Hub}
        return address_vertices_dic, vertices_address_dic


# It will get the vertex associated with the addresses of the packages of truck one
# Big O notation of O(n)
def get_vertices_truck1():
    address_dictionary, _ = get_address_vertices()  # it will take the address_vertices dictionary
    truck1_vertices = []  # it will hold the addresses vertices value for truck one

    # get the address index for packages
    for i in truck_one:
        truck1_vertices.append(address_dictionary[i.package_address])  # it will append just the vertex that is present
        # on truck one

    return list(set(truck1_vertices))  # remove duplicates, because in some cases more than one package will be
    # delivered in the same address


# It does the same thing of the above function, but for the truck two
# Big O notation O(n)
def get_vertices_truck2():
    address_dictionary, _ = get_address_vertices()
    truck2_vertices = []

    # get the address index for  packages
    for i in truck_two:
        truck2_vertices.append(address_dictionary[i.package_address])
    return list(set(truck2_vertices))  # remove duplicates, because in some cases more than one package will be
    # delivered in the same address


# Again, it will do the same of the above function, but for truck three
# Big O notation O(n)
def get_vertices_truck3():
    address_dictionary, _ = get_address_vertices()
    truck3_vertices = []
    for i in truck_three:
        if i.package_id == 9:  # here It will correct the address for package 9
            i.package_address = "410 S State St"
            i.package_zip = "84111"
        truck3_vertices.append(address_dictionary[i.package_address])
    return list(set(truck3_vertices))


# It will return the packages in truck one
# Big O notation O(1)
def get_truck_one_packages():
    return truck_one


# It will return the packages in truck two
# Big O notation O(1)
def get_truck_two_packages():
    return truck_two


# It will return the packages in truck three
# Big O notation O(1)
def get_truck_three_packages():
    return truck_three


# It will return all the packages
# Big O notation O(1)
def get_all_packages():
    return all_package
