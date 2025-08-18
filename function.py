def calculate_discount(discount_percent, price):
    buying = (price * ((100 - discount_percent)/100))

    if discount_percent >= 20:
        return buying 
        
    elif discount_percent <20:
        return price
    else:
        pass

print(calculate_discount(price = int(input("Enter original price:")), discount_percent = int(input("Enter the discount:"))))