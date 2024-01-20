class Menu:
    def __init__(self):
        self.menu_items = {
            '1': {'name': 'Paneer', 'price': 10.99},
            '2': {'name': 'Pizza', 'price': 14.99},
            '3': {'name': 'Pasta', 'price': 8.99},
            '4': {'name': 'Salad', 'price': 5.99},
        }

    def display_menu(self):
        print("Menu:")
        print("---------------")
        print("Item\tName\tPrice")
        print("---------------")
        for item, details in self.menu_items.items():
            print(f"{item}\t{details['name']}\t${details['price']}")
        print("---------------")

class Order:
    def __init__(self):
        self.order_items = {}

    def add_item(self, item_id, quantity):
        if item_id in self.order_items:
            self.order_items[item_id]['quantity'] += quantity
        else:
            self.order_items[item_id] = {'quantity': quantity}

    def display_order(self, menu):
        if not self.order_items:
            print("Your order is empty.")
        else:
            print("Your Order:")
            print("---------------")
            print("Item\tName\tQuantity\tPrice")
            print("---------------")
            total_price = 0
            for item_id, details in self.order_items.items():
                menu_item = menu.menu_items[item_id]
                item_price = menu_item['price'] * details['quantity']
                total_price += item_price
                print(f"{item_id}\t{menu_item['name']}\t{details['quantity']}\t\t${item_price:.2f}")
            print("---------------")
            print(f"Total\t\t\t\t${total_price:.2f}")
            print("---------------")

class HotelManagementSystem:
    def __init__(self):
        self.menu = Menu()
        self.order = Order()

    def display_main_menu(self):
        print("\nHotel Management System:")
        print("1. View Menu")
        print("2. Place Order")
        print("3. View Order")
        print("4. Generate Bill")
        print("5. Exit")

    def run(self):
        while True:
            self.display_main_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.menu.display_menu()

            elif choice == '2':
                self.menu.display_menu()
                item_id = input("Enter the item ID to order: ")
                quantity = int(input("Enter the quantity: "))
                self.order.add_item(item_id, quantity)
                print("Item added to the order.")

            elif choice == '3':
                self.order.display_order(self.menu)

            elif choice == '4':
                self.order.display_order(self.menu)
                print("Bill generated. Thank you!")

            elif choice == '5':
                print("Exiting Hotel Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    hotel_system = HotelManagementSystem()
    hotel_system.run()
