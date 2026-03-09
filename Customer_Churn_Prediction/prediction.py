import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings("ignore")
data = pd.read_csv("Churn_Modelling.csv")
data = data.drop(["RowNumber", "CustomerId", "Surname"], axis=1)
label_encoder = LabelEncoder()
data["Gender"] = label_encoder.fit_transform(data["Gender"])
data["Geography"] = label_encoder.fit_transform(data["Geography"])
X = data.drop("Exited", axis=1)
y = data["Exited"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Training Random Forest Model...")
model = RandomForestClassifier(n_estimators=200,random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Training Completed")
print("Model Accuracy:", accuracy)
print("\nEnter Customer Details:")
credit_score = int(input("Credit Score: "))
geography = int(input("Geography (0=France, 1=Germany, 2=Spain): "))
gender = int(input("Gender (0=Female, 1=Male): "))
age = int(input("Age: "))
tenure = int(input("Tenure (years with bank): "))
balance = float(input("Account Balance: "))
num_products = int(input("Number of Products: "))
has_card = int(input("Has Credit Card? (1=Yes, 0=No): "))
active_member = int(input("Is Active Member? (1=Yes, 0=No): "))
salary = float(input("Estimated Salary: "))
customer_data = [[
    credit_score,
    geography,
    gender,
    age,
    tenure,
    balance,
    num_products,
    has_card,
    active_member,
    salary
]]
probability = model.predict_proba(customer_data)[0][1]
print("\nChurn Probability:", probability)
if probability > 0.5:
    print("Prediction: Customer likely to leave the bank.")
else:
    print("Prediction: Customer likely to stay.")






#OUTPUT
#1
#Training Random Forest Model...
#Model Training Completed
#Model Accuracy: 0.865

#Enter Customer Details:
#Credit Score: 6000
#Geography (0=France, 1=Germany, 2=Spain): 0
#Gender (0=Female, 1=Male): 0
#Age: 26
#Tenure (years with bank): 4
#Account Balance: 50000
#Number of Products: 2
#Has Credit Card? (1=Yes, 0=No): 1
#Is Active Member? (1=Yes, 0=No): 1
#Estimated Salary: 30000

#Churn Probability: 0.135
#Prediction: Customer likely to stay.





#2
#Training Random Forest Model...
#Model Training Completed
#Model Accuracy: 0.865

#Enter Customer Details:
#Credit Score: 5000
#Geography (0=France, 1=Germany, 2=Spain): 2
#Gender (0=Female, 1=Male): 1
#Age: 25
#Tenure (years with bank): 3
#Account Balance: 50000
#Number of Products: 3
#Has Credit Card? (1=Yes, 0=No): 1
#Is Active Member? (1=Yes, 0=No): 1
#Estimated Salary: 70000

#Churn Probability: 0.52
#Prediction: Customer likely to leave the bank.
