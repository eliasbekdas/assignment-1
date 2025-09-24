# Prompt user for product name
product = input("What's the product name? ").strip().lower()

# Use if/elif instead of match-case for compatibility
if product in ("electronics", "gadget") or product.startswith("tech"):
    category = "High Margin"
elif product in ("clothing", "apparel"):
    category = "Medium Margin"
elif product in ("food", "grocery"):
    category = "Low Margin"
else:
    category = "Uncategorized - Review Needed"

# Print result
print(f"Product: {product} | Category: {category}")
