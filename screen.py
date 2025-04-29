from abc import ABC, abstractmethod

# ----- Guitar Classes -----
class Guitar(ABC):
    def __init__(self, brand, model, wood_type, string_count, body_size):
        self.brand = brand
        self.model = model
        self.wood_type = wood_type
        self.string_count = string_count
        self.body_size = body_size

    @abstractmethod
    def get_description(self):
        pass

class Acoustic(Guitar):
    def __init__(self, brand, model, wood_type, string_count, body_size, acoustic_type, price):
        super().__init__(brand, model, wood_type, string_count, body_size)
        self.acoustic_type = acoustic_type
        self.price = price

    def get_description(self):
        return (f"[Acoustic] {self.brand} {self.model} | {self.acoustic_type} | "
                f"{self.wood_type}, {self.string_count} strings | ${self.price}")

class Electric(Guitar):
    def __init__(self, brand, model, wood_type, string_count, body_size, pickup_type, price):
        super().__init__(brand, model, wood_type, string_count, body_size)
        self.pickup_type = pickup_type
        self.price = price

    def get_description(self):
        return (f"[Electric] {self.brand} {self.model} | {self.pickup_type} pickups | "
                f"{self.wood_type}, {self.string_count} strings | ${self.price}")
        

# ----- Store and Cart Classes -----
class Store:
    def __init__(self):
        self.inventory = []

    def add_guitar(self, guitar):
        self.inventory.append(guitar)

    def show_inventory(self):
        print("\n--- Available Guitars ---")
        for i, guitar in enumerate(self.inventory, 1):
            print(f"{i}. {guitar.get_description()}")

    def get_guitar(self, index):
        if 0 <= index < len(self.inventory):
            return self.inventory[index]
        return None

class Cart:
    def __init__(self):
        self.items = []

    def add(self, guitar):
        self.items.append(guitar)
        print(f"Added to cart: {guitar.brand} {guitar.model}")

    def view(self):
        print("\n--- Cart ---")
        total = 0
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.get_description()}")
            total += item.price
        print(f"Total: ${total}")
        return total

    def clear(self):
        self.items.clear()


# ----- Main System -----
def main():
    store = Store()
    cart = Cart()

    # Sample inventory
    store.add_guitar(Acoustic("Yamaha", "FG800", "Spruce", 6, "Full", "Dreadnought", 200))
    store.add_guitar(Electric("Fender", "Stratocaster", "Alder", 6, "Full", "Single Coil", 1200))
    store.add_guitar(Electric("PRS", "Silver Sky", "Mahogany", 6, "Full", "Humbucker", 2300))

    while True:
        print("\n--- Guitar Shop ---")
        print("1. View Inventory")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Clear Cart")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            store.show_inventory()

        elif choice == "2":
            store.show_inventory()
            try:
                idx = int(input("Select guitar number to add to cart: ")) - 1
                guitar = store.get_guitar(idx)
                if guitar:
                    cart.add(guitar)
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            cart.view()

        elif choice == "4":
            total = cart.view()
            if total == 0:
                print("Cart is empty.")
            else:
                confirm = input("Confirm checkout? (y/n): ")
                if confirm.lower() == "y":
                    with open("receipt.txt", "w") as file:
                        file.write("--- Receipt ---\n")
                        for item in cart.items:
                            file.write(f"{item.get_description()}\n")
                        file.write(f"Total: ${total}\n")
                    print("Order placed! Receipt saved to 'receipt.txt'.")
                    cart.clear()

        elif choice == "5":
            cart.clear()
            print("Cart cleared.")

        elif choice == "0":
            print("Thanks for visiting!")
            break

        else:
            print("Invalid option. Try again.")

main()