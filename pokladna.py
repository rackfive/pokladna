def main():
    total_price = 666
    payment = 1000
    available_cash = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

    # Control check
    if total_price > payment:
        print("Nedostatek peněz!")
    elif payment not in available_cash:
        print("Neplatná hodnota bankovky nebo mince!")
    else:
        # Calculate and print the returned cash
        returned_cash = calculate_change(total_price, payment, available_cash)
        print("Vrátit:", returned_cash)

# Function to calculate the returned cash
def calculate_change(total_price, payment, available_cash):
    # Calculate the amount to be returned
    change = payment - total_price
    returned_cash = []

    # Loop for each available cash type
    for cash in available_cash:
        while change >= cash:
            # Insert cash to return into the list
            returned_cash.append(cash)
            # Reduce the amount to change
            change -= cash

    return returned_cash

if __name__ == "__main__":
    main()
