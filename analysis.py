import pandas as pd

# # Using the read_csv function from the panda module to access the dataset
# data = pd.read_csv(".\data\women_clothing_ecommerce_sales.csv")
# print(data.head())

# Loading the first 5 rows of the dataset while using the read_csv function from the panda module
data = pd.read_csv(".\data\women_clothing_ecommerce_sales.csv")
# print("Displaying the first 5 rows of dataset:")
# print(data.head())

# Create a copy of my dataset to work with
data_copy = data.copy()
print(data_copy.head())

# Inspecting the dataset - Checking for missing values using the isnull() and sum() combo
# print("Number of missing values in each column:")
# print(data.isnull().sum())

# Fill missing 'size' values with the most frequent size
# most_frequent_size = data['size'].mode()[0]
# data['size'].fillna(most_frequent_size, inplace=True)
