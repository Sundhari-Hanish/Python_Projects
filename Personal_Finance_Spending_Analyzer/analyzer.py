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
