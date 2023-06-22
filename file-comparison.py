import os
import pandas as pd

# Prompt the user to enter the directory paths
dir1 = input("Newest directory: ")
dir2 = input("Complete directory as gold standard to compare for missing files: ")

# Get the filenames in the directories
files1 = set(os.listdir(dir1))
files2 = set(os.listdir(dir2))

# Get the filenames that are present in dir1 but not in dir2
diff1 = files1 - files2

# Get the filenames that are present in dir2 but not in dir1
diff2 = files2 - files1

# Create a DataFrame with the results
df = pd.DataFrame({'present_in': [dir1]*len(diff1) + [dir2]*len(diff2),
                   'filename': list(diff1) + list(diff2)})

# Write the DataFrame to a CSV file
df.to_csv(dir1 + 'file_comparison.csv', index=False)

print(f"Comparison results written to file_comparison.csv")