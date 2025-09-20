class Product:
    inventory = []
    product_counter = 0

    def __init__(self, product_id, name, category, quantity, price, supplier, ):
        self.product_id = product_id
        self.name = name
        self.catgeory = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        cls.product_counter += 1
        new_product = Product(cls.product_counter, name, category, quantity, price, supplier)
        cls.inventory.append(new_product)
        return "Product added successfully!"

    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        product = next((p for p in Product.inventory if p.product_id == product_id), None)
        if not product:
            print(f"Product with ID {product_id} not found.")
            return
        if quantity is not None:
            product.quantity = quantity
        if price is not None:
            product.price = price
        if supplier:
            product.supplier = supplier
        return "Product information updated successfully."

    def delete_product(product_id):
        product = next((p for p in Product.inventory if p.product_id == product_id), None)
        if not product:
            print(f"Product with ID {product_id} not found.")
            return
        Product.inventory.remove(product)
        return "Product deleted successfully."
    
class Order:
    def __init__(self, order_id, product_id, quantity, customer_info):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.customer_info = customer_info
  
    def place_order(self):
        for product in Product.inventory:
            if product.product_id == self.product_id:
                if product.quantity >= self.quantity:
                    product.quantity -= self.quantity
                    return f"Order placed successfully. Order ID: {self.order_id}"
                else:
                    return "Insufficient stock."
            else:
                return "Product not found."

print(Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A"))
print(Product.add_product("T-Shirt", "Clothing", 100, 25, "Supplier B"))
print(Product.update_product(1, quantity=45, price=950))
print(Product.delete_product(2))
order1 = Order(order_id=1, product_id=1, quantity=2, customer_info="John Doe")
print(order1.place_order())
