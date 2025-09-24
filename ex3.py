# Define a function to format greeting
def format_greeting(name, title="Customer"):
    # Strip whitespace from both ends of the string
    name = name.strip()
    
    # Handle empty name input
    if not name:
        return "Hello, Valued Customer!"
    
    # Convert to title case (first letter capitalized for each word)
    name = name.title()
    
    # Split the string into words (first name is the first element)
    first_name = name.split()[0]
    
    # Return formatted greeting
    return f"Hello, {first_name} ({title})!"

# Main code
full_name = input("What's your full name? ")
greeting = format_greeting(full_name)  # Uses default title "Customer"
print(greeting)
