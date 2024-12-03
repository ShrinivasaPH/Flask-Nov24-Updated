import requests

url = 'http://127.0.0.1:5000/predict'

data = {
    "ApplicantIncome": 100,
    "Credit_History": 1.0,
    "Gender": "Male",
    "LoanAmount": 12000,
    "Married": "No"
}

x = requests.post(url, json=data)
print(x.text)