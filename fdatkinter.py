import tkinter as tk
from tkinter import ttk

class Node:
    def __init__(self, name, order_number, destination_address, phone_number, food_order):
        self.prev = None
        self.name = name
        self.order_number = order_number
        self.destination_address = destination_address
        self.phone_number = phone_number
        self.food_order = food_order
        self.next = None

class FoodDeliveryApp:
    def __init__(self):
        self.head = None
        self.tail = None

    def place_order(self, name, order_number, destination_address, phone_number, food_order):
        if self.head is None:
            self.head = Node(name, order_number, destination_address, phone_number, food_order)
            self.tail = self.head
        else:
            new_node = Node(name, order_number, destination_address, phone_number, food_order)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display_orders(self):
        current_node = self.head
        orders_info = []
        while current_node:
            order_info = f"Name: {current_node.name}\nOrder Number: {current_node.order_number}\nDestination Address: {current_node.destination_address}\nPhone Number: {current_node.phone_number}\nFood Order: {current_node.food_order}\n"
            orders_info.append(order_info)
            current_node = current_node.next
        return orders_info

    def remove_order(self, order_number):
        current_node = self.head

        while current_node:
            if current_node.order_number == order_number:
                prev_node = current_node.prev
                next_node = current_node.next

                if prev_node:
                    prev_node.next = next_node
                else:
                    self.head = next_node

                if next_node:
                    next_node.prev = prev_node
                else:
                    self.tail = prev_node

                del current_node
                return True

            current_node = current_node.next

        return False

class FoodDeliveryAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Delivery App")

        self.app = FoodDeliveryApp()

        self.create_widgets()

    def create_widgets(self):
        # GUI components
        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(row=0, column=0, columnspan=4, pady=10)

        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Place Order")

        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Display Orders")

        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Remove Order")

        # Tab 1 - Place Order
        ttk.Label(self.tab1, text="Name:").grid(row=0, column=0)
        self.name_entry = ttk.Entry(self.tab1)
        self.name_entry.grid(row=0, column=1)

        ttk.Label(self.tab1, text="Order Number:").grid(row=1, column=0)
        self.order_number_entry = ttk.Entry(self.tab1)
        self.order_number_entry.grid(row=1, column=1)

        ttk.Label(self.tab1, text="Destination Address:").grid(row=2, column=0)
        self.destination_address_entry = ttk.Entry(self.tab1)
        self.destination_address_entry.grid(row=2, column=1)

        ttk.Label(self.tab1, text="Phone Number:").grid(row=3, column=0)
        self.phone_number_entry = ttk.Entry(self.tab1)
        self.phone_number_entry.grid(row=3, column=1)

        ttk.Label(self.tab1, text="Food Order:").grid(row=4, column=0)
        self.food_order_entry = ttk.Entry(self.tab1)
        self.food_order_entry.grid(row=4, column=1)

        ttk.Button(self.tab1, text="Place Order", command=self.place_order).grid(row=5, column=0, columnspan=2, pady=10)

        # Tab 2 - Display Orders
        self.display_text = tk.Text(self.tab2, height=10, width=40)
        self.display_text.grid(row=0, column=0, pady=10)

        # Tab 3 - Remove Order
        ttk.Label(self.tab3, text="Order Number to Remove:").grid(row=0, column=0)
        self.remove_order_entry = ttk.Entry(self.tab3)
        self.remove_order_entry.grid(row=0, column=1)

        ttk.Button(self.tab3, text="Remove Order", command=self.remove_order).grid(row=1, column=0, columnspan=2, pady=10)

    def place_order(self):
        name = self.name_entry.get()
        order_number = self.order_number_entry.get()
        destination_address = self.destination_address_entry.get()
        phone_number = self.phone_number_entry.get()
        food_order = self.food_order_entry.get()

        self.app.place_order(name, order_number, destination_address, phone_number, food_order)
        self.display_orders()
        self.clear_place_order_entries()

    def display_orders(self):
        orders = self.app.display_orders()
        self.display_text.delete(1.0, tk.END)
        for order in orders:
            self.display_text.insert(tk.END, order + "\n")

    def remove_order(self):
        order_number = self.remove_order_entry.get()
        removed = self.app.remove_order(order_number)
        if removed:
            self.display_orders()
            tk.messagebox.showinfo("Success", f"Order {order_number} removed successfully!")
        else:
            tk.messagebox.showwarning("Error", f"Order {order_number} not found.")

    def clear_place_order_entries(self):
        self.name_entry.delete(0, tk.END)
        self.order_number_entry.delete(0, tk.END)
        self.destination_address_entry.delete(0, tk.END)
        self.phone_number_entry.delete(0, tk.END)
        self.food_order_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app_gui = FoodDeliveryAppGUI(root)
    root.mainloop()
