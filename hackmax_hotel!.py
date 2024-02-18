#hack Matrix
#class created
'''    class fooditems to rake input for the food detail form the donor '''
class FoodItem:
    def __init__(self, name, quantity, expiry_date, selling_cost=0):
        self.name = name
        self.quantity = quantity
        self.expiry_date = expiry_date
        self.selling_cost = selling_cost
'''  donor class to to store donor details and food details from the user '''
class Donor:
    #function to add name 
    def __init__(self, name):
        self.name = name
        self.inventory = [] 
    # inventory list to store the no of the donors and their id to use for further computation  
    #function to add food item
    # listing down the food details 
    def donate_food(self, name, quantity, expiry_date, selling_cost):
        food_item = FoodItem(name, quantity, expiry_date, selling_cost)
        self.inventory.append(food_item)
        print(f"{quantity} units of {name} donated by {self.name} added to ")
    #function to view directory
    # viewing the inventory details 
    def view_inventory(self):
        print(f"Inventory of {self.name}:")
        for item in self.inventory:
            print(f"Name: {item.name}, Quantity: {item.quantity}, Expiry Date: {item.expiry_date}, Selling Cost: {item.selling_cost}")
    #remove foood when order accepted
    # if any fooditem isn't accepted then we need to remove fooditem from the list before it get spolied
    def remove_food(self, name, quantity):# describing the food details to be removed
        for item in self.inventory:
            if item.name == name:
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    print(f"{quantity} units of {name} deducted from inventory of {self.name}.")
                else:
                    print(f"Not enough {name} in inventory of {self.name}.")
                break
        else:
            print(f"{self.name} does not have {name} in inventory.")
''' code for genrating recipitent reqeust and storing the food quality condition to accept the food'''
class Recipient:
    #recipitent name initialzation
    def __init__(self, name):# for storing the recepient details
        self.name = name
        self.requests = []
        self.budget = 1000
    #function to add food item
    def request_food(self, name, quantity):
        request = {"name": name, "quantity": quantity}
        self.requests.append(request)
        print(f"{quantity} units of {name} requested by {self.name}.")
    #function add budget
    def set_budget(self, budget):
        self.budget = budget
        print(f"Budget of {self.budget} set for {self.name}.")
    # function to add request 
    # function to verify the details of request and confirm the request
    def view_requests(self):
        print(f"Requests by {self.name}:")
        for request in self.requests:
            print(f"Name: {request['name']}, Quantity: {request['quantity']}")
    #accept the order
    def accept_order(self, donor, food_name, quantity):
        donor.remove_food(food_name, quantity)
        for request in self.requests:
            if request["name"] == food_name:
                if request["quantity"] >= quantity:
                    request["quantity"] -= quantity
                    print(f"{quantity} units of {food_name} accepted by {self.name}.")
                    if request["quantity"] == 0:
                        self.requests.remove(request)
                    break
        else:
            print(f"No request found for {quantity} units of {food_name} by {self.name}.")


def main():
    donors = []
    recipients = []
# taking input from the user to do the task of donor or generate recipient and displaying the possiblities pf the code 
    while True:
        print("\n1. Add Donor")
        print("2. Donate Food")
        print("3. View Donor Inventory")
        print("4. View Full Donor List")
        print("5. Add Your Nmae to Recipient Restaurant")
        print("6. Set Recipient Budget")
        print("7. Request Food")
        print("8. View Recipient Restautrant Requests")
        print("9. Accept Order")
        print("10. Exit")

        choice = input("\nEnter your choice: ")
# using the above function to manage the waste food
        if choice == '1':
            donor_name = input("Enter your name: ")
            donor = Donor(donor_name)
            donors.append(donor)
            print(f"{donor_name} added to the donor list.")

        elif choice == '2':
            donor_name = input("Enter donor name: ")
            for donor in donors:
                if donor.name == donor_name:
                    food_name = input("Enter food name: ")
                    quantity = int(input("Enter quantity: "))
                    expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
                    selling_cost = float(input("Enter selling cost: "))
                    donor.donate_food(food_name, quantity, expiry_date, selling_cost)
                    break
            else:
                print("Donor not found.")
                print("Add your name to donor restaurant's list")

        elif choice == '3':
            donor_name = input("Enter donor name: ")
            for donor in donors:
                if donor.name == donor_name:
                    donor.view_inventory()
                    break
            else:
                print("Donor not found.")

        elif choice == '4':
            print("\nFull Donor List:")
            for donor in donors:
                print(donor.name)

        elif choice == '5':
            recipient_name = input("Enter recipient name: ")
            recipient = Recipient(recipient_name)
            recipients.append(recipient)
            print(f"{recipient_name} added to the recipient list.")

        elif choice == '6':
            recipient_name = input("Enter recipient name: ")
            budget = float(input("Enter expected budget: "))
            for recipient in recipients:
                if recipient.name == recipient_name:
                    recipient.set_budget(budget)
                    break
            else:
                print("Recipient not found.")
                print("Add your name to donor restaurant's list")


        elif choice == '7':
            recipient_name = input("Enter recipient name: ")
            for recipient in recipients:
                if recipient.name == recipient_name:
                    food_name = input("Enter food name: ")
                    quantity = int(input("Enter quantity: "))
                    recipient.request_food(food_name, quantity)
                    break
            else:
                print("Recipient not found.")

        elif choice == '8':
            recipient_name = input("Enter recipient name: ")
            for recipient in recipients:
                if recipient.name == recipient_name:
                    recipient.view_requests()
                    break
            else:
                print("Recipient not found.")

        elif choice == '9':
            recipient_name = input("Enter recipient name: ")
            donor_name = input("Enter donor name: ")
            food_name = input("Enter food name: ")
            quantity = int(input("Enter quantity: "))
            for recipient in recipients:
                if recipient.name == recipient_name:
                    for donor in donors:
                        if donor.name == donor_name:
                            recipient.accept_order(donor, food_name, quantity)
                            break
                    break
            else:
                print("Recipient or donor not found.")

        elif choice == '10':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

# by the use of main function taking the choice from the user to manage fooditems according their need.
if __name__ == "__main__":
    main()
