from flask import Flask, jsonify,request
import configparser
import os
import requests
import datetime
import base64
import json
import io
from pathlib import Path
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/predict', methods=['POST'])
def predict_disease():
    try:
        values = request.get_json()
        medical_text=values["medical_text"]
        model = SimpleT5()
        for file in glob("./outputs/*"):
            if 'epoch-1' in file:
                last_epoch_model = file
        model.load_model("t5", last_epoch_model, use_gpu=False)
        predictions = []
        prediction = model.predict(medical_text)[0] 
        description=""
        print(prediction) 
        print(type(prediction))      
        if prediction== "1":
            description="Digestive system diseases"
        elif prediction=="2":
            description="cardiovascular diseases"
        elif prediction=="3":
            description="neoplasms"
        elif prediction=="4":
            description="nervous system disease"
        elif prediction=="5":
            description="General pathological conditions "
        else:
            description="Undefined condition"   
        result={"Category":prediction,"Description":description,"medical text":medical_text}
        print(result)
        return json.dumps(result)
    except Exception as  e:
        print(e)
        result={"Error":"Not able to process your request."}
        return json.dumps(result)



if __name__ == '__main__':

    currentDirectory = os.getcwd()
    config = configparser.RawConfigParser()
    config.read(os.path.join(currentDirectory, 'PythonDeploy.cfg'))
    port = config['DEPLOY']['port']
    host = config['DEPLOY']['host']
    
    print(host, port)
    app.run(host=host, port=port, threaded=True)    