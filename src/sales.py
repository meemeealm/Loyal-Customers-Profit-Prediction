import requests

url = 'http://127.0.0.1:8000/predict'

sales = {
  "Customer Name": "Harish",
  "Sub Category": "Health Drinks",
  "City": "Vellore",
  "Discount": 4,
  "Sales": 10
}

response = requests.post(url, json=sales)
prediction = response.json()

predicted_profit = prediction["predicted_profit"]

print('predicted profit =', predicted_profit)

if predicted_profit <= 200:
    print("Lower than 200")
else:
    print("Higher than 200")