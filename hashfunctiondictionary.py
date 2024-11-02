stock_prices = {}
with open("C:\\Users\\beaul\\Desktop\\stock_prices.csv", "r") as f:
    for line in f:
        print(repr(line))  # Print the raw line for debugging
        tokens = line.split(';')  # Use semicolon as the delimiter

        if len(tokens) < 2:  # Check if the line has enough tokens
            print("Skipping line:", line)  # Print the problematic line
            continue  # Skip to the next line

        day = tokens[0].strip()  # Strip any whitespace
        price = float(tokens[1].strip())  # Convert the price to float
        stock_prices[day] = price
    # Print the entire stock prices list
    print(stock_prices)

    # this operation is O(1)
    print(f'stockprices with dictionary: {stock_prices['09/Mar']}')
