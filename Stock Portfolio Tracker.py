stocks = {
    "HBL": 250,
    "UBL": 300,
    "MCB": 280,
    "BAHL": 90,
    "MEBL": 230
}

total = 0

print("Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stocks.keys()))

while True:
    stock = input("Enter stock name or type done: ").upper()

    if stock == "DONE":
        break

    if stock not in stocks:
        print("This stock is not in the list.")
        continue

    quantity = input("Enter quantity: ")

    if not quantity.isdigit():
        print("Please enter a number.")
        continue

    quantity = int(quantity)

    investment = stocks[stock] * quantity
    total = total + investment

    print("Investment for", stock, "is:", investment)

print("Total investment:", total)
print("Thank you for using the stock tracker.")