# List of lists example
table_data = [
    ["Ticker", "Open", "Close"],
    ["AAPL", 363.25, 363.4],
    ["AMZN", 2756.0, 2757.99],
    ["GOOG", 1409.1, 1408.2]
]

# Access the Amazon data
amazon_data = table_data[2]

# Get the Amazon opening price
amazon_opening_price = amazon_data[1]

# Combine the previous 2 steps
amazon_opening_price = table_data[2][1]

# Print out the ticker data by row
for row in table_data:
    print(row)

# List of dictionaries example
table_data = [
    {
        "Ticker": "AAPL",
        "Open": 363.25,
        "Close": 363.4
    },
    {
        "Ticker": "AMZN",
        "Open": 2756.0,
        "Close": 2757.99
    },
    {
        "Ticker": "GOOG",
        "Open": 1409.1,
        "Close": 1408.2
    }
]

# Print out each dictionary in the list
for data in table_data:
    print(data)

# Print out just the ticker value in each dictionary in the list
for data in table_data:
    print(data["Ticker"])
