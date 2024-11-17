import streamlit as st

# Sample menu data
menu = [
    {"name": "Pizza", "price": 50},
    {"name": "Burger", "price": 60},
    {"name": "Pasta", "price": 70}
]

# Function to display menu
def display_menu():
    st.write("## Menu")
    for item in menu:
        st.write(f"{item['name']} - ${item['price']}")

# Function to add a new menu item
def add_menu_item():
    with st.form(key='add_menu_form'):
        name = st.text_input("Item Name")
        price = st.number_input("Price", min_value=0.0, format="%.2f")
        submit_button = st.form_submit_button(label='Add Item')
        
        if submit_button:
            new_item = {"name": name, "price": price}
            menu.append(new_item)
            st.success(f"Added {name} to the menu!")

# Function to take orders
def take_order():
    st.write("## Order")
    order_items = []
    
    for item in menu:
        if st.checkbox(item['name']):
            order_items.append(item)
    
    if st.button("Place Order"):
        total = sum(item['price'] for item in order_items)
        st.write("### Your Order")
        for item in order_items:
            st.write(f"{item['name']} - ${item['price']}")
        st.write(f"**Total: ${total}**")
        st.success("Order placed successfully!")

# Streamlit app layout
def main():
    st.title("Restaurant Management System")
    
    menu_option = st.sidebar.selectbox(
        "Select an option",
        ["Menu", "Add Menu Item", "Order"]
    )
    
    if menu_option == "Menu":
        display_menu()
    elif menu_option == "Add Menu Item":
        add_menu_item()
    elif menu_option == "Order":
        take_order()

if __name__ == "__main__":
    main()

