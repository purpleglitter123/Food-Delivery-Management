import pytest
from tkinter import Tk
from food_delivery_app import FoodDeliveryApp, FoodDeliveryAppGUI

@pytest.fixture
def app():
    return FoodDeliveryApp()

def test_place_order(app):
    app.place_order("John Doe", "123", "123 Main St", "555-1234", "Pizza")
    assert app.head.name == "John Doe"
    assert app.head.order_number == "123"
    assert app.head.destination_address == "123 Main St"
    assert app.head.phone_number == "555-1234"
    assert app.head.food_order == "Pizza"

def test_display_orders(app, capsys):
    app.place_order("John Doe", "123", "123 Main St", "555-1234", "Pizza")
    app.place_order("Jane Doe", "124", "456 Oak St", "555-5678", "Burger")

    app.display_orders()

    captured = capsys.readouterr()
    expected_output = "Name: John Doe\nOrder Number: 123\nDestination Address: 123 Main St\nPhone Number: 555-1234\nFood Order: Pizza\n" \
                      "Name: Jane Doe\nOrder Number: 124\nDestination Address: 456 Oak St\nPhone Number: 555-5678\nFood Order: Burger\n"
    assert captured.out == expected_output

def test_remove_order(app):
    app.place_order("John Doe", "123", "123 Main St", "555-1234", "Pizza")
    app.place_order("Jane Doe", "124", "456 Oak St", "555-5678", "Burger")

    assert app.remove_order("123")
    assert app.head.order_number != "123"

    assert not app.remove_order("999")  # Non-existent order

def test_gui_place_order():
    root = Tk()
    app_gui = FoodDeliveryAppGUI(root)

    app_gui.name_entry.insert(0, "John Doe")
    app_gui.order_number_entry.insert(0, "123")
    app_gui.destination_address_entry.insert(0, "123 Main St")
    app_gui.phone_number_entry.insert(0, "555-1234")
    app_gui.food_order_entry.insert(0, "Pizza")

    app_gui.place_order()

    assert app_gui.app.head.name == "John Doe"
    assert app_gui.app.head.order_number == "123"
    assert app_gui.app.head.destination_address == "123 Main St"
    assert app_gui.app.head.phone_number == "555-1234"
    assert app_gui.app.head.food_order == "Pizza"

def test_gui_remove_order():
    root = Tk()
    app_gui = FoodDeliveryAppGUI(root)

    app_gui.app.place_order("John Doe", "123", "123 Main St", "555-1234", "Pizza")
    app_gui.app.place_order("Jane Doe", "124", "456 Oak St", "555-5678", "Burger")

    app_gui.remove_order_entry.insert(0, "123")
    app_gui.remove_order()

    assert app_gui.app.head.order_number != "123"

    app_gui.remove_order_entry.delete(0, tk.END)
    app_gui.remove_order_entry.insert(0, "999")  # Non-existent order
    app_gui.remove_order()

    assert app_gui.app.head.order_number != "999"

if __name__ == "__main__":
    pytest.main()
