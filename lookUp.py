import readPackages
import datetime

hash_table = readPackages.get_hash_table()


# this function will return the package choose by the user
# pack_id is the value input by the user
# Big O notation of O(N)
def lookUp_id(pack_id):
    for i in range(1, 41):
        item = hash_table.search(i)
        if item.package_id == pack_id:
            print("Package id:", item.package_id,
                  "Delivery address:", item.package_address, " ", item.package_city, " ", item.package_state, " ",
                  item.package_zip,
                  "Package weight :", item.package_kg,
                  "Delivery deadline: ", item.package_deadline,
                  "Delivery at: ", datetime.timedelta(minutes=item.package_delivery))
    print(" ")
    next_action()


# this function will show the package delivery status according to a time choose by the user
# if the time input is earlier than 8:00 AM all the packages will be at Hub (except package 6 and 25 which will
# be in route
# if the package delivered time is > than input time the delivery status will depends of which truck the package is
# Big O notation of O(n)
def lookUp_time(input_time):
    for i in range(1, 41):
        item = hash_table.search(i)
        if input_time < 8 * 60:
            item.package_delivery = "At Hub"
        if (item.package_id == 25 or item.package_id == 6) and input_time < (9 * 60) + 5:
            item.package_delivery = "In transit"
        if isinstance(item.package_delivery, float):
            if item.package_delivery > input_time:
                # packages on truck one
                if item.package_id in [14, 15, 16, 34, 20, 21, 19, 1, 7, 29, 37, 30, 13, 39, 27, 35]:
                    item.package_delivery = "Out for delivery"
                # packages on truck two
                if item.package_id in [25, 26, 22, 24, 28, 4, 40, 31, 32, 17, 6, 36, 12, 18, 38, 3]:
                    if input_time < (9 * 60) + 10:
                        item.package_delivery = "At Hub"
                    if input_time >= (9 * 60) + 10:
                        item.package_delivery = "Out for delivery"
                # packages on truck three
                if item.package_id in [2, 33, 10, 5, 23, 8, 9, 11]:
                    if input_time < (11 * 60):
                        item.package_delivery = "At Hub"
                    if input_time >= (11 * 60):
                        item.package_delivery = "Out for delivery"

        # if the package was already delivered, this code block will format it to 24h format to show to the user
        if isinstance(item.package_delivery, float):
            time_formated = datetime.timedelta(minutes=item.package_delivery)
            item.package_delivery = time_formated

        print("Package id:", item.package_id,
              "Delivery address:", item.package_address, "", item.package_city, "", item.package_state, "",
              item.package_zip,
              "Package weight :", item.package_kg,
              "Delivery deadline:", item.package_deadline,
              "Delivery status: ", item.package_delivery)

    print(" ")
    next_action()


# this function will give the next steps function
# the user can choose to go back to the main and execute another search or it can exit the program
# Big O notation of O(1)
def next_action():
    print("Select from the following : ")
    print("1 = Return to main screen ")
    print("2 = Exit the program ")
    #
    user_input = input()
    if user_input == "1":
        import subprocess
        subprocess.call("main.py", shell=True)
    else:
        exit()
