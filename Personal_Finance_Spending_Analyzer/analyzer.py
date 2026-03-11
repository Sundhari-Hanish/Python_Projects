import pandas as pd
import matplotlib.pyplot as plt
import random
import warnings
warnings.filterwarnings("ignore")
data = pd.read_csv("budget_data.csv")
merchants = ["Amazon", "Flipkart", "Grocery Store", "Local Market", "Restaurant", "Netflix"]
data["Merchant"] = [random.choice(merchants) for _ in range(len(data))]
payment_methods = ["Cash", "Credit Card", "Debit Card", "UPI"]
data["Payment_Method"] = [random.choice(payment_methods) for _ in range(len(data))]
data.rename(columns={"date": "Transaction_Date"}, inplace=True)
data["Transaction_Date"] = pd.to_datetime(data["Transaction_Date"])
data = data.dropna()
data["Month"] = data["Transaction_Date"].dt.to_period("M")
monthly_spending = data.groupby("Month")["amount"].sum()
print("\nMonthly Spending Report:")
print(monthly_spending.to_string())
category_spending = data.groupby("category")["amount"].sum()
print("\nCategory-wise Spending:")
print(category_spending.to_string())
plt.figure(figsize=(10,5))
monthly_spending.plot(kind="bar", color="skyblue")
plt.title("Monthly Spending Report")
plt.xlabel("Month")
plt.ylabel("Total Amount")
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(7,7))
category_spending.plot(kind="pie", autopct="%1.1f%%", startangle=140)
plt.title("Spending by Category")
plt.ylabel("")
plt.show()



#OUTPUT:
# Monthly Spending Report:
# Month
# 2022-07    2861.38
# 2022-08    1307.52
# 2022-09    1338.48
# 2022-10    2001.12
# 2022-11    1017.81
# 2022-12    1605.53
# 2023-01    2162.19
# 2023-02    1540.84
# 2023-03    2274.61
# 2023-04    2224.88
# 2023-05    2599.92
# 2023-06    1935.36
# 2023-07    5192.72
# 2023-08    1123.74
# 2023-09    1629.95
# 2023-10    1728.26
# 2023-11    1428.31
# 2023-12    1810.44
# 2024-01    4068.93
# 2024-02    1250.66
# 2024-03    1559.18
# 2024-04    1706.30
# 2024-05    4021.46
# 2024-06    2644.02
# 2024-07    5509.49
# 2024-08    2194.54
# 2024-09    3068.27
# Freq: M

# Category-wise Spending:
# category
# Business lunch        2503.01
# Clothing              4365.50
# Coffe                 9350.70
# Communal              4192.50
# Events                2751.30
# Film/enjoyment          34.34
# Fuel                   114.00
# Health                5896.50
# Learning              2525.31
# Market                6451.03
# Motel                  675.00
# Other                 1045.75
# Phone                  666.08
# Rent Car                95.00
# Restuarant           10425.60
# Sport                 1436.76
# Taxi                   865.08
# Tech                  2985.00
# Transport              746.70
# Travel                3756.45
# business_expenses      400.00
# joy                    524.30
