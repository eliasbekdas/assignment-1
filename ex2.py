# Prompt the user for credit score (int, assume 300-850 range).
score = int(input("Enter your credit score: "))

# Check validity first
if score < 300 or score > 850:
    print("Invalid score.")
else:
    if score >= 750:
        print("Excellent - Loan Approved. Interest rate: Low")
    elif 700 <= score < 750:
        print("Good - Loan Approved with Review. Interest rate: Low")
    elif 600 <= score < 700:
        print("Fair - Loan Conditional. Seek credit improvement.")
    else:  # score < 600
        print("Poor - Loan Denied. Seek credit improvement.")
