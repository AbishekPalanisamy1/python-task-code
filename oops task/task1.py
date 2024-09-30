class Product:
    def __init__(self, name, price, quantity=1):
     
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
      
        return f"{self.name} - Price: {self.price}, Quantity: {self.quantity}"

    def get_total_price(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        
        self.cart = {}

    def add_product(self, product):
       
        if product.name in self.cart:
            # Update the quantity of the product if it's already in the cart
            self.cart[product.name].quantity += product.quantity
        else:
            # Add the product to the cart
            self.cart[product.name] = product
        print(f"Added {product.quantity} of {product.name} to the cart.")

    def remove_product(self, product_name):
       
        if product_name in self.cart:
            del self.cart[product_name]
            print(f"Removed {product_name} from the cart.")
        else:
            print(f"{product_name} not found in the cart.")

    def calculate_total(self):
        
        total = sum(product.get_total_price() for product in self.cart.values())
        return total

    def display_cart(self):
        
        if not self.cart:
            print("The cart is empty.")
        else:
            print("Shopping Cart:")
            for product in self.cart.values():
                print(product)


if __name__ == "__main__":
   
    product1 = Product("Laptop", 1200.00, 1)
    product2 = Product("Smartphone", 800.00, 2)
    product3 = Product("Headphones", 150.00, 1)

    # Create a shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_product(product1)
    cart.add_product(product2)
    cart.add_product(product3)

    # Display the cart
    cart.display_cart()

    # Calculate the total price
    print(f"Total: ${cart.calculate_total()}")

    # Add more of an existing product
    product4 = Product("Laptop", 1200.00, 1)
    cart.add_product(product4)

    # Display the updated cart
    cart.display_cart()

    # Calculate the updated total price
    print(f"Total: ${cart.calculate_total():.2f}")

    # Remove a product
    cart.remove_product("Smartphone")

    # Display the cart after removing a product
    cart.display_cart()

    # Final total price
    print(f"Total: ${cart.calculate_total():.2f}")
