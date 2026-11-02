products = []
count = int(input("Number of products: "))

for i in range(count):
    product_id = input("Product ID: ")
    price = float(input("Price: "))
    stock = int(input("Stock quantity: "))
    products.append((product_id, price, stock))

for product_id, price, stock in products:
    if price < 0 or stock < 0:
        print(product_id, "Invalid record")
    else:
        print(product_id, "Inventory value:", price * stock)
        if stock < 5:
            print("Replenishment needed")