# import libs
import pandas as pd
import sklearn 
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__ , template_folder='template')

@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/predict', methods=['GET','POST'])
def predict():
    
    if request.method == 'POST':
        var1 = int(request.form['GrLivArea'])
        var2 = int(request.form['OverallQual'])
        var3 = int(request.form['KitchenQual'])
        var4 = float(request.form['GarageArea'])
        var5 = float(request.form['GarageCars'])
        var6 = float(request.form['TotalBsmtSF'])
        var7 = int(request.form['ExterQual'])
        var8 = int(request.form['1stFlrSF'])
        var9 = int(request.form['BsmtQual'])
        var10 = int(request.form['GarageFinish'])
        var11 = int(request.form['FullBath'])
        var12 = int(request.form['TotRmsAbvGrd'])
        var13 = int(request.form['Foundation_PConc'])
        var14 = int(request.form['2ndFlrSF'])
        var15 = float(request.form['BsmtFinSF1'])
        var16 = int(request.form['Fireplaces'])
        var17 = int(request.form['LotArea'])
        var18 = float(request.form['LotFrontage'])
        var19 = float(request.form['MasVnrArea'])
        var20 = int(request.form['BsmtFinType1'])
        #preddata = pd.DataFrame([[var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11,var12,var13,var14,var15,var16,var17,var18,var19,var20]],columns = ['var1', 'var2', 'var3', 'var4', 'var5', 'var6', 'var7', 'var8', 'var9', 'var10', 'var11','var12','var13','var14','var15','var16','var17','var18','var19','var20'])
        preddata = pd.DataFrame({
    'GrLivArea': [var1],
    'OverallQual': [var2],
    'KitchenQual': [var3],
    'GarageArea': [var4],
    'GarageCars': [var5],
    'TotalBsmtSF': [var6],
    'ExterQual': [var7],
    '1stFlrSF': [var8],
    'BsmtQual': [var9],
    'GarageFinish': [var10],
    'FullBath': [var11],
    'TotRmsAbvGrd': [var12],
    'Foundation_PConc': [var13],
    '2ndFlrSF': [var14],
    'BsmtFinSF1': [var15],
    'Fireplaces': [var16],
    'LotArea': [var17],
    'LotFrontage': [var18],
    'MasVnrArea': [var19],
    'BsmtFinType1': [var20]
})
        
        readmodel = open('Regmodel.pkl','rb')
        model = pickle.load(readmodel)
        

        result = model.predict(preddata)
        print(result)

    else:
        result = 0 
    return render_template('Predict.html',res = result)
if __name__ == '__main__':
    app.run(port=5001, debug=True)