class Product:
    inventory = []                                                                                  # Creates a list for the products
    product_counter = 0                                                                             # Allows for the assignment of product IDs

    def __init__(self, product_id, name, category, quantity, price, supplier, ):                    # Creates the parameters for the products
        self.product_id = product_id
        self.name = name
        self.catgeory = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):                                # Adds products into the inventory
        cls.product_counter += 1                                                                    # Increments the product counter for every added product
        new_product = Product(cls.product_counter, name, category, quantity, price, supplier) 
        cls.inventory.append(new_product)                                                           # Adds the product into the list 
        return "Product added successfully!"

    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):                  # Updates existing products in the inventory
        product = next((x for x in Product.inventory if x.product_id == product_id), None)          # Checks for the requested product ID
        if not product:
            print(f"Product with ID {product_id} not found.")                                       # Prints if the requested product ID does not exist
            return
        if quantity is not None:                                                                    # Checks for values in the quantity parameter
            product.quantity = quantity
        if price is not None:                                                                       # Checks for values in the price parameter 
            product.price = price
        if supplier:                                                                                # Checks for values in the supplier parameter
            product.supplier = supplier
        return "Product information updated successfully."                                          # Prints if the product information was successfully updated

    def delete_product(product_id):
        product = next((x for x in Product.inventory if x.product_id == product_id), None)          # Checks for the requested product ID
        if not product:
            print(f"Product with ID {product_id} not found.")                                       # Prints if the requested product ID does not exist
            return
        Product.inventory.remove(product)
        return "Product deleted successfully."                                                      # Prints if the product was successfully deleted
    
class Order:
    def __init__(self, order_id, product_id, quantity, customer_info):                              # Creates the parameters for the orders
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.customer_info = customer_info
  
    def place_order(self):
        for product in Product.inventory:                                                           
            if product.product_id == self.product_id:                                               # Checks for the requested product ID
                if product.quantity >= self.quantity:
                    product.quantity -= self.quantity                                               # Decreases the product's quantity by the requested amount
                    return f"Order placed successfully. Order ID: {self.order_id}"                  # Prints if the order was placed successfully
                else:
                    return "Insufficient stock."                                                    # Prints if the product's quantity is insufficient
            else:
                return "Product not found."                                                         # Prints if the requested product ID does not exist

print(Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A"))
print(Product.add_product("T-Shirt", "Clothing", 100, 25, "Supplier B"))
print(Product.update_product(1, quantity=45, price=950))
print(Product.delete_product(2))
order1 = Order(order_id=1, product_id=1, quantity=2, customer_info="John Doe")
print(order1.place_order())
