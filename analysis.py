import pandas as pd

# Load dataset
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'])

# -------------------------------
# 1. Total Sales
# -------------------------------
print("\n🔹 Total Sales:")
print(df['Sales'].sum())

# -------------------------------
# 2. Category-wise Sales
# -------------------------------
print("\n🔹 Category-wise Sales:")
category_sales = df.groupby('Category')['Sales'].sum()
print(category_sales)

# -------------------------------
# 3. Category-wise Profit
# -------------------------------
print("\n🔹 Category-wise Profit:")
category_profit = df.groupby('Category')['Profit'].sum()
print(category_profit)

# -------------------------------
# 4. Furniture Discount Check
# -------------------------------
print("\n🔹 Furniture Data (Sales, Profit, Discount):")
furniture_data = df[df['Category'] == 'Furniture']
print(furniture_data[['Sales', 'Profit', 'Discount']].head())

# -------------------------------
# 5. Region-wise Sales
# -------------------------------
print("\n🔹 Region-wise Sales:")
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print(region_sales)

# -------------------------------
# 6. Region-wise Profit
# -------------------------------
print("\n🔹 Region-wise Profit:")
region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
print(region_profit)

# -------------------------------
# 7. Top 10 Products by Sales
# -------------------------------
print("\n🔹 Top 10 Products by Sales:")
top_products_sales = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_products_sales)

# -------------------------------
# 8. Top 10 Products by Profit
# -------------------------------
print("\n🔹 Top 10 Products by Profit:")
top_products_profit = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
print(top_products_profit)
import matplotlib.pyplot as plt

# Category-wise Sales & Profit
category_sales = df.groupby('Category')['Sales'].sum()
category_profit = df.groupby('Category')['Profit'].sum()

# Plot
plt.figure()

category_sales.plot(kind='bar', label='Sales')
category_profit.plot(kind='bar', label='Profit')

plt.title("Sales vs Profit by Category")
plt.xlabel("Category")
plt.ylabel("Amount")

plt.legend()
plt.show()
# Average discount per category
avg_discount = df.groupby('Category')['Discount'].mean()

print("\n🔹 Average Discount by Category:")
print(avg_discount)