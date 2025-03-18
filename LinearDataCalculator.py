import csv
import numpy as np

def calculate_slope_from_csv(filepath):
    # Read the third column ("Wert") from the CSV file
    x_values = []
    y_values = []
    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Skip the header
        for row in reader:
            x_values.append(float(row[0]))  # First column: Original Wert
            y_values.append(float(row[2].replace(',', '.')))  # Third column: Wert

    # Perform linear regression to calculate the slope
    x = np.array(x_values)
    y = np.array(y_values)
    A = np.vstack([x, np.ones(len(x))]).T
    slope, _ = np.linalg.lstsq(A, y, rcond=None)[0]
    return slope

if __name__ == "__main__":
    csv_filepath = "./TestdataLinear.CSV"  # Updated to relative path
    slope = calculate_slope_from_csv(csv_filepath)
    print(f"The slope of the best-fit line is: {slope}")
