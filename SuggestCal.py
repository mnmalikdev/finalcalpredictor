import numpy as np
import pandas as pd
from flask import Flask
from sklearn import linear_model

app = Flask(__name__)
       
@app.route("/getCalories",methods=['GET','POST'])
def SuggestWeeklyCalories():
    # read csv file using pandas
    df = pd.read_csv('./finalDataAI.csv',dtype=str)
    df.astype(str, errors='ignore')
    # print(df.to_string())
    X=df[['TDEE','Goal',	'Weekly Drop',	'Body Fat']]
    Y=df['Suggested Cals']
    # convert df to float
    print("error here at this point")

    
    # create linear regression object
    regr = linear_model.LinearRegression()
    
    regr.fit(X, Y)
    predictedWeeklyCals = regr.predict([[2457,1,1.2,16]])
    # round of predictedWeeklyCals to nearest floating point
    predictedWeeklyCals = round(predictedWeeklyCals[0])
    print(predictedWeeklyCals)
    # convert to response instance for flask

    return str(predictedWeeklyCals)


