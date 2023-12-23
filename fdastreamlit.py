import streamlit as st

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
            order_info = {
                "Name": current_node.name,
                "Order Number": current_node.order_number,
                "Destination Address": current_node.destination_address,
                "Phone Number": current_node.phone_number,
                "Food Order": current_node.food_order
            }
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


# Initialize the session state
session_state = st.session_state
if not hasattr(session_state, "app"):
    session_state.app = FoodDeliveryApp()

# Streamlit UI
st.title("Food Delivery App")

menu_options = ["Place Order", "Display Orders", "Remove Order"]
selected_menu = st.sidebar.selectbox("Select Option", menu_options)

if selected_menu == "Place Order":
    name = st.text_input("Name:")
    order_number = st.text_input("Order Number:")
    destination_address = st.text_input("Destination Address:")
    phone_number = st.text_input("Phone Number:")
    food_order = st.text_area("Food Order:")
    
    if st.button("Place Order"):
        session_state.app.place_order(name, order_number, destination_address, phone_number, food_order)
        st.success("Order Placed Successfully!")

elif selected_menu == "Display Orders":
    orders = session_state.app.display_orders()
    if orders:
        st.table(orders)
    else:
        st.info("No orders to display.")

elif selected_menu == "Remove Order":
    order_number_to_remove = st.text_input("Order Number to Remove:")
    if st.button("Remove Order"):
        removed = session_state.app.remove_order(order_number_to_remove)
        if removed:
            st.success(f"Order {order_number_to_remove} Removed Successfully!")
        else:
            st.warning(f"Order {order_number_to_remove} not found.")

# Note: This Streamlit app is a simplified example and may need further adjustments based on your requirements.
