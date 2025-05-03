from product import Product

# Create a product
pen = Product("Pens", 2.5, 20)
pen.display_info()

# Add and remove inventory
pen.add_inventory(10)
pen.remove_inventory(5)

print("\nAfter update:")
pen.display_info()
