from __future__ import print_function
from flask import Flask, request, render_template,jsonify
import os
#hold temp path to import identicon module
import sys
sys.path.append("../identicon")
#Import identicon generator as a module 
from identicon import Identicon


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text = request.form['text']
    word = request.args.get('text')

    #function_output = main(text)
    #function_output = do_something(text) 
    function_output = Identicon.do_something3(text)  

    result = {
        "output": function_output
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)


if __name__ == '__main__':
    app.run( debug=True)






'''
#----------------------------------------------------------------
#for trial 

@app.route("../identicon/output/<text>.png")
def getImage(text):
    # get image binary from MongoDB, which is bson.Binary type
    function_output = Identicon.image_to_file(text)  

    result = {
        "output": function_output
    }
    result = {str(key): value for key, value in result.items()}

    return 'text' + ".png"
    
#----------------------------------------------------------------
#for trial 

from flask import send_file
@app.route('/get_image')
def get_image():
    filename = 'output\\123.jpg'
    return send_file(filename, mimetype='image/jpg')

#----------------------------------------------------------------
#for trial

def do_something(text):
    text = text+text
    function_output = text
    return function_output

#-------------------------------------------------------------------
#for trial

def do_something2(num1):
    num1 = int(num1)
    num2 = (num1)*5
    df = pd.DataFrame(np.random.randn(num2,num1))
    df = df.to_json()
    function_output = df
    return function_output    

#-------------------------------------------------------------------
'''







