from typing import List, Dict, Optional

class Cap:
    def __init__(self, cap_id: int, name: str, price: float, quantity: int) -> None:
        self.cap_id = cap_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"ID: {self.cap_id}, Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"

class Inventory:
    def __init__(self) -> None:
        self.caps: Dict[int, Cap] = {}

    def add_cap(self, cap_id: int, name: str, price: float, quantity: int) -> None:
        if cap_id in self.caps:
            print(f"Cap ID {cap_id} already exists. Please use a unique ID.")
        else:
            self.caps[cap_id] = Cap(cap_id, name, price, quantity)
            print(f"Cap '{name}' added to inventory.")

    def update_cap(self, cap_id: int, name: Optional[str] = None, price: Optional[float] = None, quantity: Optional[int] = None) -> None:
        cap = self.caps.get(cap_id)
        if cap:
            if name:
                cap.name = name
            if price is not None:
                cap.price = price
            if quantity is not None:
                cap.quantity = quantity
            print(f"Cap ID {cap_id} updated.")
        else:
            print(f"Cap ID {cap_id} not found in inventory.")

    def remove_cap(self, cap_id: int) -> None:
        if cap_id in self.caps:
            removed_cap = self.caps.pop(cap_id)
            print(f"Cap '{removed_cap.name}' removed from inventory.")
        else:
            print(f"Cap ID {cap_id} not found in inventory.")

    def display_inventory(self) -> None:
        if not self.caps:
            print("Inventory is empty.")
        else:
            print("\nCurrent Inventory:")
            for cap in self.caps.values():
                print(cap)

def main() -> None:
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Cap")
        print("2. Update Cap")
        print("3. Remove Cap")
        print("4. Display Inventory")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            cap_id = int(input("Enter Cap ID: "))
            name = input("Enter Cap Name: ")
            price = float(input("Enter Cap Price: "))
            quantity = int(input("Enter Cap Quantity: "))
            inventory.add_cap(cap_id, name, price, quantity)

        elif choice == '2':
            cap_id = int(input("Enter Cap ID to update: "))
            name = input("Enter new name (leave blank to keep current): ") or None
            price_input = input("Enter new price (leave blank to keep current): ")
            price = float(price_input) if price_input else None
            quantity_input = input("Enter new quantity (leave blank to keep current): ")
            quantity = int(quantity_input) if quantity_input else None
            inventory.update_cap(cap_id, name, price, quantity)

        elif choice == '3':
            cap_id = int(input("Enter Cap ID to remove: "))
            inventory.remove_cap(cap_id)

        elif choice == '4':
            inventory.display_inventory()

        elif choice == '5':
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
