class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def update_membership(self, new_membership):
        print("calculation costs")
        self.membership_type = new_membership

    def __str__(self):
        print("converting to string")
        return self.name + " " + self.membership_type

    def __eq__(self, other):
        if self.name == other.name and other.membership_type == self.membership_type:
            return True

        return False

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    __hash__ = None

    __repr__ = __str__


customers = [Customer("Amir", "Bronze"),
             Customer("Skandar", "Gold")]

print(customers)

# class.method(list)
Customer.print_all_customers(customers)

print(customers[0] == customers[1])


print(customers[0])


customers[0].update_membership("Gold")
customers[1].membership_type = "7did"
print(customers[0].membership_type)
print(customers[1].membership_type)
