import pandas as pd

# Using the read_csv function from the panda module to access the dataset
data = pd.read_csv(".\data\women_clothing_ecommerce_sales.csv")
print(data.head())