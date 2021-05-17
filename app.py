
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn import metrics
from flask import Flask, request, render_template, redirect, url_for
import re
import math
import pickle

app = Flask("__name__")

q = ""

@app.route("/")
def loadPage():
	return render_template('HOME.html', query="")



@app.route("/", methods=['POST'])
def Predict():
   
 

    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']
    inputQuery7 = request.form['query7']
    inputQuery8 = request.form['query8']
    inputQuery9 = request.form['query9']

    model = pickle.load(open("model.pkl","rb"))
    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7, inputQuery8, inputQuery9]]
    
    
    # Create the pandas DataFrame 
    new_df = pd.DataFrame(data, columns = ['age','gender','cigsPerDay','prevalentHyp','heartRate','BMI','sysBP','diaBP','glucose'])
    single = model.predict(new_df)
    probability1 = model.predict_proba(new_df)[:,1]
    probability2 = model.predict_proba(new_df)[:,0]
    
    if single==1:
        RESULT = "THE PATIENT CAN BE DIAGNOSED WITH HEART DISEASE"
        PROB = " {}".format(probability1*100)
    else:
        RESULT = "THE PATIENT CAN BE SAFE"
        PROB = " {} ".format(probability2*100)
    
    #return render_template('output.html', output1=RESULT, output2=PROB, query1 = request.form['query1'], query2 = request.form['query2'], query3 = request.form['query3'], query4 = request.form['query4'], query5 = request.form['query5'], query6 = request.form['query6'], query7 = request.form['query7'], query8 = request.form['query8'], query9 = request.form['query9'])
    return render_template('output.html', output1=RESULT, output2=PROB,query1 = inputQuery1,query2 = inputQuery2,query3 = inputQuery3,query4 = inputQuery4,query5 = inputQuery5,query6 = inputQuery6,query7 = inputQuery7,query8 = inputQuery8,query9 = inputQuery9)
if __name__ == '__main__':
    app.debug = True
    app.run()