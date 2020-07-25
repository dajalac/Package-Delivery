from loadTruck import get_truck_one_packages
from loadTruck import get_truck_two_packages
from loadTruck import get_truck_three_packages
import readPackages
import datetime

hash_table = readPackages.get_hash_table()

truck_one = get_truck_one_packages()
truck_two = get_truck_two_packages()
truck_three = get_truck_three_packages()

class LookUp :

    # def luckUp_id(id):
    #     for i in all_packages:
    #         item = hash_table.search(i.package_id)
    #         if item.package_id == id:
    #             print("Package id:", item.package_id,
    #                   "Delivery address:", item.package_address, " ", item.package_city, " ", item.package_state, " ",
    #                   item.package_zip,
    #                   "Package weight :", item.package_kg,
    #                   "Delivery deadline: ", item.package_deadline,
    #                   "Delivery status: ", item.package_delivery)

    def lookUp_time(self,input_time):
        # copy of original list
        # transforar input in minutes

        for i in range(1, 41):
            item = hash_table.search(i)
            # print("input time", input_time)
            if input_time < 8 * 60:
                # print("antes de tudo", item.package_delivery)
                item.package_delivery = "At Hub"
            if (item.package_id == 25 or item.package_id == 6) and input_time < (90 * 60) + 5:
                item.package_delivery = "In transit"
            #     print("item delivery < q as 8",item.package_delivery)
            # print("it is string", item.package_delivery is not str)
            # print("o delivery time", item.package_delivery)
            if isinstance(item.package_delivery, float):
                # print ("IS IS NOT A STRING", item.package_delivery)
                if item.package_delivery > input_time:
                    if item.package_id in [14, 15, 16, 34, 20, 21, 19, 1, 7, 29, 37, 30, 13, 39, 27, 35]:
                        item.package_delivery = "Out for delivery"
                    if item.package_id in [25, 26, 22, 24, 28, 4, 40, 31, 32, 17, 6, 36, 12, 18, 38, 3]:
                        if input_time < (9 * 60) + 10:
                            item.package_delivery = "At Hub"
                            # print("no truck 2  < 9:10", item.package_delivery)
                            # print(" ")
                        if input_time > (9 * 60) + 10:
                            item.package_delivery = "Out for delivery"
                            # print("no truck 2  > 9:10", item.package_delivery)
                            # print(" ")
                    if item.package_id in [2, 33, 10, 5, 23, 8, 9, 11]:
                        if input_time < (11 * 60):
                            item.package_delivery = "At Hub"
                            # print("no truck 3  < 11", item.package_delivery)
                            # print(" ")
                        if input_time > (11 * 60):
                            item.package_delivery = "Out for delivery"
                            # print("no truck 3  < 11", item.package_delivery)
                            # print(" ")

            if isinstance(item.package_delivery, float):
                time_formated = datetime.timedelta(minutes=item.package_delivery)
                item.package_delivery = time_formated

            print("Package id:", item.package_id,
                  "Delivery address:", item.package_address, " ", item.package_city, " ", item.package_state, " ",
                  item.package_zip,
                  "Package weight :", item.package_kg,
                  "Delivery deadline: ", item.package_deadline,
                  "Delivery status: ", item.package_delivery)

            print(" ")
            self.next_action()


    def next_action(self):
        print("Select from the following : ")
        print("1 = Return to main menu ")
        print("2 = Exit the program ")

        user_input = input()
        if user_input == 1:
            exec(open("main.py").read())
