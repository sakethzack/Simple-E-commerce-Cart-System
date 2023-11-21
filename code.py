class Product:
    def __init__(self, name, price, available):
        self.name = name
        self.price = price
        self.available = available
        self.discount_percentage = 0

    def set_discount(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def get_discounted_price(self):
        return self.price * (1 - self.discount_percentage / 100)

    def __str__(self):
        available_status = "Available" if self.available else "Not Available"
        discount_info = f" (Discount: {self.discount_percentage}%)" if self.discount_percentage > 0 else ""
        return f"{self.name} - ${self.price}, {available_status}{discount_info}"

class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity=1):
        if product.name in self.items:
            self.items[product.name]['quantity'] += quantity
        else:
            self.items[product.name] = {'product': product, 'quantity': quantity}

    def remove_product(self, product_name):
        if product_name in self.items:
            del self.items[product_name]

    def update_quantity(self, product_name, quantity):
        if product_name in self.items:
            self.items[product_name]['quantity'] = quantity

    def calculate_total(self):
        return sum(item['product'].get_discounted_price() * item['quantity'] for item in self.items.values())

    def __str__(self):
        return '\n'.join([f"{item['quantity']} x {item['product']}" for item in self.items.values()])

# Creating an initial catalog of products
products = {}

# Initialize cart
cart = Cart()

# CLI for the cart and product system
while True:
    print("\nCommands: add_product, view_catalog, add_to_cart, remove, update, view_cart, checkout, quit")
    command = input("Enter command: ").lower()

    if command == 'add_product':
        name = input("Enter new product name: ")
        price = float(input("Enter product price: "))
        available = input("Is the product available (yes/no)? ").lower() == 'yes'
        products[name] = Product(name, price, available)
        print(f"Added new product: {name}")

    elif command == 'view_catalog':
        print("Product Catalog:")
        for product_name, product in products.items():
            print(product)

    elif command == 'add_to_cart':
        product_name = input("Enter product name to add to cart: ")
        if product_name in products:
            quantity = int(input("Enter quantity: "))
            discount = int(input("Enter discount percentage (0 for no discount): "))
            product = products[product_name]
            product.set_discount(discount)
            cart.add_product(product, quantity)
            print(f"Added {quantity} x {product_name} (Discount: {discount}%) to cart.")
        else:
            print("Product not found.")

    elif command == 'remove':
        product_name = input("Enter product name to remove from cart: ")
        cart.remove_product(product_name)
        print(f"Removed {product_name} from cart.")

    elif command == 'update':
        product_name = input("Enter product name to update quantity: ")
        quantity = int(input("Enter new quantity: "))
        cart.update_quantity(product_name, quantity)
        print(f"Updated quantity for {product_name} in cart.")

    elif command == 'view_cart':
        print("Cart items:")
        print(cart)

    elif command == 'checkout':
        print("Cart items:")
        print(cart)
        print(f"Total bill (after discounts): ${cart.calculate_total()}")
        break

    elif command == 'quit':
        break

    else:
        print("Invalid command.")
