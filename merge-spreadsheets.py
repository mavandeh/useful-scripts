# merge-spreadsheets.py: Written with assistance from ChatGPT

import glob
import pandas as pd
import os

def read_files(directory):
    """
    Reads all .xls and .csv files in the specified directory into a single pandas dataframe.
    """
    # Find all .xls and .csv files in the specified directory
    filenames = glob.glob(f'{directory}/*.xls') + glob.glob(f'{directory}/*.csv') + glob.glob(f'{directory}/*.xlsx')

    # Create an empty list to store the dataframes
    df_list = []

    # Loop through the filenames and read each file into a dataframe
    for file in filenames:
        # Skip directories
        if not os.path.isdir(file):
            # Split the file extension from the filename
            filename, file_extension = os.path.splitext(file)

            # Check the file extension and read the file into a dataframe
            if file_extension == '.xls':
                df = pd.read_excel(file, engine='xlrd')
            elif file_extension == '.xlsx':
                df = pd.read_excel(file)
                print("found .xlsx")
            elif file_extension == '.csv':
                df = pd.read_csv(file)
            else:
                df = None
            #print(f'Original dataframe: {df}')

            # Check if any of the columns of the dataframe contain 'Unnamed'
            if df.columns.str.contains('Unnamed').any():
                # Reread the file with header=0
                if file_extension == '.xls':
                    df = pd.read_excel(file, engine='xlrd', header=1)
                elif file_extension == '.xlsx':
                    df = pd.read_excel(file, header=1)
                elif file_extension == '.csv':
                    df = pd.read_csv(file, header=1)
                else:
                    df = None
                #print(f'Dataframe with Unnamed columns: {df}')
            
            # Check if the first cell has data and the rest of the cells are blank, if so delete row
            df = df[df.iloc[:, 1:].notnull().any(axis=1)]

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
