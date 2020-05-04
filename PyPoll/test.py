import pandas as pd

# Save path to data set in a variable
data_file = "Resources/dataSet.csv"

# Use Pandas to read data
data_file_df = pd.read_csv(data_file)
data_file_df.head()