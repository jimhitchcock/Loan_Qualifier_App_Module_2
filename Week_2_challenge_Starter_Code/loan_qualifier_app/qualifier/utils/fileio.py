# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(csvpath, data):
    """Saves the CSV file from path provided.

    Args:
        csvpath (Path): The CSV file path.
        data (list of lists): A list of the rows of data for the CSV file.
        header (list): An optional header for the CSV.

    """
    header = ["Bank","Credit Score","Debt","Income","Loan Amount","Home Value"]     # Header values
    output_path = csvpath                                                    # Create variable to be filled by user input with questionary      
    with open(output_path, "w", newline="") as csvfile:                             # 
        cheap_loans = csv.writer(csvfile)
        cheap_loans.writerow(header)
        cheap_loans.writerows(data)
