# defining functions for actions I want to reuse
def get_price(entry):
    return float(entry.split(":")[1])


def get_year(entry):
    return int(entry.split("-")[2][:4])


def get_month(entry):
    return int(entry.split("-")[0])


def display_monthly_averages(data):
    monthly_sums = {}
    monthly_counts = {}

    for entry in data:
        year = get_year(entry)
        month = get_month(entry)
        price = get_price(entry)

        key = f"{month:02d}-{year}"
        monthly_sums[key] = monthly_sums.get(key, 0) + price
        monthly_counts[key] = monthly_counts.get(key, 0) + 1

    # printing the output of monthly averages for all the data
    # returns a long list of averages for each month
    print("The monthly average price is as follows:")
    for key in sorted(monthly_sums.keys()):
        month, year = key.split("-")
        average = monthly_sums[key] / monthly_counts[key]
        print(f"Average price for {month}-{year}: ${average:.2f}")


# find the lowest price in the data
def lowest_element_position(data):
    min_pos = 0
    min_price = get_price(data[0])

    for i in range(1, len(data)):
        price = get_price(data[i])
        if price < min_price:
            min_price = price
            min_pos = i

    return min_pos


# bonus for creating a new file with the data sorted from lowest to highest
def create_low_to_high_file(data):
    sorted_data = []

    while data:
        min_pos = lowest_element_position(data)
        sorted_data.append(data.pop(min_pos))

    with open("low to high.txt", "w") as file:
        for entry in sorted_data:
            file.write(entry)


# main function that calls the other functions
def main():
    with open("GasPrices.txt", "r") as file:
        content = file.readlines()

    data = [line.strip() for line in content]

    display_monthly_averages(data)
    create_low_to_high_file(
        data
    )  # Remove this line if you don't want to create the "low to high.txt" file.


if __name__ == "__main__":
    main()
