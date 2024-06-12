    # Lists and Dictionaries 

# Create while loop to ensure numeric input
    # Create variable for menu units
while True:
    menu_units = input("Enter the number of items on your menu: ")
    if menu_units.isnumeric():
        break
    else: print("Error: Please Enter a Valid Number")

# Create empty list for menu item input
# Create empty list for price input
# Create empty list for stock input
menu = []
price_list = []
stock_list = []
# for number of menu units
    #  Create variable to store menu item input
    # append menu item input to menu list
for i in range(0, int((menu_units))):
    menu_input = input("Add a menu item: \n")    
    menu.append(menu_input)
    # Create while loop to ensure numeric input
        # Create variable to store price input
        #  append price input to price list
    while True:
        price_unit = input("Enter the price per unit: ")
        if price_unit.isnumeric():
            price_list.append(price_unit)
            break
        elif price_unit.replace(".", "").isnumeric():
            price_list.append(price_unit)
            break
        else:
            print("Error: Please Enter a Valid Number")
    # Create while loop to ensure numeric input
        # Create variable to store stock input
        #  append stock input to stock list
    while True:
        stock_unit = input("Enter the stock count: ") 
        if stock_unit.isnumeric():
            stock_list.append(stock_unit)
            break
        elif stock_unit.replace(".", "").isnumeric():
            stock_list.append(stock_unit)
            break
        else: 
            print("ERROR: Please Enter a Valid Number")

price_list = [float(price_unit) for price_unit in price_list]

stock_list = [float(stock_unit) for stock_unit in stock_list]


# Create stock dictionary with key menu items 
# Creat price dicctionary with key menu items 
stock = dict(zip(menu, stock_list))
price = dict(zip(menu, price_list))


print("Below is the value of your stock by item: \n")

# Create variable for total stock value
total_stock = 0

# for each item in stock
    # Create variable to store total price of each menu item
    # add item price to stock value count with each iteration
# Display value of total stock   
for item in stock:
    item_price = (price[item] * stock[item])
    print(f" {item} : £{item_price}")
    total_stock = total_stock + item_price
print(f" \n The total value of your stock is:  £{total_stock}")
   

# Terminate 
exit()

