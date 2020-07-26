# class to store the packages as objects
# big O notation of O(1)


class Packages:
    def __init__(self, package_id, package_address, package_city, package_state, package_zip,
                 package_deadline, package_kg, package_special_notes, delivery_status=0):
        self.package_id = package_id
        self.package_address = package_address
        self.package_city = package_city
        self.package_state = package_state
        self.package_zip = package_zip
        self.package_deadline = package_deadline
        self.package_kg = package_kg
        self.package_special_note = package_special_notes
        self.package_delivery = delivery_status
