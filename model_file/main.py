#!/usr/bin/env python
# coding: utf-8
# In[1]:
from flask import Flask, request, jsonify, render_template
import pickle 
import numpy as np
import sklearn
# In[2]:
#change the save path location for model.bin depends on your computer
save_path = r"C:\Users\nguye\Desktop\Data Science Stuff\Projects\Python\Flask\model_file\model.bin"
# # Deployment of Flask
# In[3]:
app = Flask(__name__)
with open(save_path,'rb') as f:
    model = pickle.load(f)
# In[4]:
@app.route("/")
def home():
    return render_template("index.html")
# In[5]:
@app.route('/',methods=['POST'])
def predict():
    int_features = [ int (x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0],2)
    return render_template('index.html', prediction_text='House Price should be $ {:,}'.format(output))
# In[ ]:
if __name__ == '__main__':
    app.run(port=5000, debug=True)





