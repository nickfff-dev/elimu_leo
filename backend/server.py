from flask import Flask
import smtplib, ssl
from flask import request
from flask import jsonify
from flask import render_template
import json
from flask import make_response



app = Flask(__name__)
# Setting up CORS headers





# mail api route
@app.route('/api/backend', methods=['GET','POST'])
def bookdata():
    
    # data = get data from json file
    with open('E:/books/bookprice/sampledata.json', 'r', encoding = "utf8") as f:
        # send each object to react ui
        data = json.load(f)
        return jsonify(data)
    


        

            



    





if __name__ == '__main__':

   app.run(debug=True)
    
   

