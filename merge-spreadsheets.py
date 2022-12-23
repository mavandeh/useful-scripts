# Written with assistance from ChatGPT

import glob
import pandas as pd
import os

def read_files(directory):
    """
    Reads all .xls and .csv files in the specified directory into a single pandas dataframe.
    """
    # Find all .xls and .csv files in the specified directory
    filenames = glob.glob(f'{directory}/*.xls') + glob.glob(f'{directory}/*.csv')

    # Create an empty list to store the dataframes
    df_list = []

    # Loop through the filenames and read each file into a dataframe
    for file in filenames:
        # Skip directories
        if not os.path.isdir(file):
            # Skip files with the same name as the output spreadsheet
            if os.path.basename(file) != 'merged-spreadsheet.csv':
                # Split the file extension from the filename
                filename, file_extension = os.path.splitext(file)
                # Check the file extension and read the file into a dataframe
                if file_extension == '.xls':
                    df = pd.read_excel(file, engine='xlrd')
                elif file_extension == '.csv':
                    df = pd.read_csv(file)
                else:
                    df = None
                # Check if the first line of the dataframe looks like column labels
                if df is not None and all(df.iloc[0].str.contains(r'[A-Za-z]', regex=True)):
                    # Remove the first line if it looks like column labels
                    df = df.iloc[1:]
                # Add a new column to the dataframe with the filename (without the directory path) and line number
                df['Source'] = f'{os.path.basename(file)} - Line {df.index+1}'
                df_list.append(df)

    # Merge all the dataframes into a single dataframe
    merged_df = pd.concat(df_list)

    return merged_df

def save_file(df, directory):
    """
    Saves the specified dataframe to a .csv file in the specified directory.
    """
    # Output the dataframe to a new file in the specified directory, overwriting the file if it already exists
    df.to_csv(f'{directory}/merged-spreadsheet.csv', index=False, mode='w')

# Prompt the user for the directory path
directory = input("Enter the directory path: ")

# Read all the files in the specified directory into a single dataframe
df = read_files(directory)

# Save the merged dataframe to a .csv file in the specified directory
save_file(df, directory)
