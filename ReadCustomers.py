import csv


def read_customers(file_path):
    customers = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            customers.append(row)
    return customers

file_path = 'customers-100.csv'  # Relative path to the CSV file
customers = read_customers(file_path)
print(customers[0]) # Print the first customer


