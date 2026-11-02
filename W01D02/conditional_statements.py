# Conditional statements (if, elif, else)
# Loops (for, while)
# Break and continue statements
# Function definition and calling
# Parameters and return values

# bool - True/ False

age = 19

if age > 18:
    print('Allowed')
    print('I entered into the club and asked for a drink')
    payment_mode = input('Card or Cash')
    print(len(payment_mode))
    if payment_mode == "Cash":
        print('Okay')
    elif payment_mode == 'Card':
        print('Swipe the Card')
else:
    print('Not Allowed')
