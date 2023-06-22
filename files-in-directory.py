import os
import pandas as pd

# Prompt the user to enter the directory paths
dir1 = input("Directory to enumerate files: ")

# Get the filenames in the directories
files1 = set(os.listdir(dir1))

# Create a DataFrame with the results
df = pd.DataFrame({'filename': list(files1)})

# Write the DataFrame to a CSV file
df.to_csv(dir1 + 'file_list.csv', index=False)

print(f"File list written to file_list.csv")