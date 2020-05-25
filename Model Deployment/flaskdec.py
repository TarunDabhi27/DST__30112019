from flask import Flask,request,jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello"

@app.route("/getPremium")
def ReturnPremium():
    premium = request.args.get('premium',type=int)
    revised_premium = premium-(0.1*premium)
    return "New Premium is"+ str(revised_premium)

if __name__=="__main__":
    app.run(debug=True)



