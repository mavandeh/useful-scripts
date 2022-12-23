# Merging Spreadsheets and .csv Files
This script merges all .xls and .csv files in a specified directory into a single .csv file.

## Collaboration
Throughout the development of this script, the user provided the following prompts:

1. Write a python script using pandas library which merges all spreadsheets and .csv files in the current directory.
2. Modify the script to take a directory input from the user, rather than the current directory.
3. Modify the script to output the merged_df to a new file in the user selected directory, filename "merged-spreadsheet.xlsx".
4. Modify the script to add a column at the end that will contain the filename and the line number from which it was copied.
5. Modify the script to ignore directories when reading files into the dataframe.
6. Modify the script to ignore files with the same name as the spreadsheet output in the last line.
7. Modify the script to output the merged dataframe as a .csv file.
8. Modify the script to ignore files with the same name as the output spreadsheet and force the last line to overwrite the file with the same name.
9. List for me again all of the prompts I've provided from working on the python script to this point.
10. Modify the script to remove handling .xlsx files due to errors thrown by the openpyxl library.
11. Modify the script to refactor the code into two functions: one that reads all .xls and .csv files in a specified directory into a single pandas dataframe, and another that saves the specified dataframe to a .csv file in a specified directory. The main script should prompt the user for the directory path and then use these two functions to read the files and save the merged dataframe.

## Usage
To use the script, run the following command:

```
python merge_spreadsheets.py
```

The script will prompt the user for the directory path. Enter the path to the directory containing the .xls and .csv files to be merged. The script will merge all the files in the specified directory into a single .csv file, adding a new column with the filename and line number of each row. The merged file will be saved as "merged-spreadsheet.csv" in the specified directory, overwriting the file if it already exists.

## Requirements
The script requires the following libraries:

* pandas
* glob
* os

## Notes
* The script ignores directories when reading files into the dataframe.
* The script ignores files with the same name as the output spreadsheet.
* The script handles .xls and .csv files only. It does not handle .xlsx files.