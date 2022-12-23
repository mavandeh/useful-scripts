# Merging Spreadsheets and .csv Files with Pandas

This script is designed to merge all spreadsheets and .csv files in a specified directory into a single dataframe using the [pandas](https://pandas.pydata.org/) library.

## Collaboration Details

Throughout the development of this script, the following prompts were provided by the user:

- Write a python script using pandas library which merges all spreadsheets and .csv files in the current directory.
- Modify the script to take a directory input from the user, rather than the current directory.
- Modify the script to output the merged dataframe to a new file in the user-selected directory, with the filename "merged-spreadsheet.xlsx".
- Modify the script to add a column at the end that will contain the filename and the line number from which it was copied.
- Modify the script to only include the filename, but not the whole directory path, in the new "Source" column.
- Modify the script to ignore directories when reading files into the dataframe.
- Modify the script to ignore files with the same name as the output spreadsheet and force the last line to overwrite the file with the same name.
- Modify the script to remove the first line of the dataframe when it imports it if it does not contain something that looks like column labels.
- Modify the script to ignore the first cell of the first line when checking for column labels.
- Modify the script to treat any cell that contains "Unnamed: " followed by any number of numbers as if it were not a column label.

**Note:** After this point the program became long enough that the output was truncated. I started asking specific questions: "Write me a line to <do this>." See commit history for further changes.

## Usage

To use this script, run the following command:

```bash
python merge_spreadsheets.py
```

The script will prompt the user to enter a directory path. Enter the path of the directory containing the spreadsheets and .csv files that you want to merge. The merged dataframe will be saved as a .csv file with the filename "merged-spreadsheet.csv" in the specified directory.

## Dependencies

This script requires the following libraries:

- [pandas](https://pandas.pydata.org/)
- [glob](https://docs.python.org/3/library/glob.html)
- [os](https://docs.python.org/3/library/os.html)

## Notes

- The script will only merge .xls and .csv files. Other file types will be ignored.
- The script will ignore directories when reading files into the dataframe.
- The script will ignore files with the same name as the output .csv file and force the last line to overwrite the file with the same name.
- The script will remove the first line of the dataframe when it imports it if it does not contain something that looks like column labels. If the dataframe has no column labels, a default column label will be added.
- The script will treat any cell that contains "Unnamed: " followed by any number of numbers as if it were not a column label when checking for column labels.
- The script will delete any row that only contains text in the first cell.
- The merged dataframe will include a new "Source" column that contains the filename (without the directory path) and line number of each row.

