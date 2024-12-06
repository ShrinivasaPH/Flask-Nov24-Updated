from flask import Flask, request
import pickle
from sklearn import sklearn

app = Flask(__name__)

model_file = open("classifier.pkl", "rb")
model = pickle.load(model_file)

#Checking Git

#Let's create endpoints....
@app.route('/', methods=['GET'])
def home():
    return "<h1>Loan Approval Application</h1>"

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    phone = 123456789
    return "<h1>Phone Number: 1234567890</h1>"

@app.route('/ping', methods=['GET'])
def ping():
    return "Hey man, why are you pinging me?"

@app.route('/aboutus', methods=['GET'])
def aboutus():
    return "We are the ML Ops learners..!!"

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':

        loan_req = request.get_json()

        if loan_req['Gender'] == 'Male':
            Gender = 0
        else:
            Gender = 1

        if loan_req['Married'] == 'No':
            Married = 0
        else:
            Married = 1
        
        ApplicantIncome = loan_req['ApplicantIncome']
        LoanAmount = loan_req['LoanAmount']
        Credit_History = loan_req['Credit_History']

        result = model.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

        if result == 0:
            pred = 'Rejected'
        else:
            pred = 'Approved'

        return {"loan_approval_status:": pred}
    else:
        return "I will make the predictions."