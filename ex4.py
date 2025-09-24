# Define a function to determine the tax bracket
def get_tax_bracket(income):
    # Handle invalid input
    if income < 0:
        return "Invalid income."
    
    # Determine bracket with conditions
    if income < 50000:
        bracket = "Low (10%)"
    elif 50000 <= income < 100000:
        bracket = "Medium (20%)"
    else:  # income >= 100000
        bracket = "High (30%)"
    
    # Bonus: Deduction eligibility check using ternary expression
    bracket = bracket + (" (Deduction Eligible)" if income % 2 == 0 else "")
    
    return bracket

# Main code
income = float(input("What's your annual income? "))
bracket = get_tax_bracket(income)

if bracket == "Invalid income.":
    print(bracket)
else:
    # Determine tax rate from bracket
    if "10%" in bracket:
        rate = 0.10
    elif "20%" in bracket:
        rate = 0.20
    else:  # "30%"
        rate = 0.30
    
    estimated_tax = income * rate
    print(f"Your bracket: {bracket}. Estimated tax: {estimated_tax:.2f}")
