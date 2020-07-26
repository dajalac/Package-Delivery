import csv
from package import Packages
from hashTable import MyHashTable

packages_list = []  # it will hold the package list from csv file

# this will read each line of the WGUPS_Package csv file and save it in the package_list
# Big O notation of O(n)
with open('WGUPS_Package.csv', 'r') as csv_file:
    readCsv = csv.reader(csv_file, delimiter=',')
    # to append each row from readCsv file into package_list
    for row in readCsv:
        packages_list.append(row)
    # create hashTable object and initialize its capacity with the packages_lis length
    hashTable = MyHashTable(sum(1 for line in packages_list))

    # add each row from package file into a package object
    # Big O notation of O(n)
    for package in packages_list:
        p = Packages(
            int(package[0]),  # id
            package[1],  # address
            package[2],  # city
            package[3],  # state
            package[4],  # zip code
            package[5],  # deadline
            package[6],  # kg
            package[7],  # special notes
        )
        # insert into hashTable
        hashTable.add(p.package_id, p)


# this will return the hash table
# Big O of O(1)
def get_hash_table():
    return hashTable
