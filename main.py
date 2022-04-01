from flask import Flask, render_template, request
import requests
import helpers

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET'])
def result():

    uprn =  request.args.get("uprn")
    valid_uprn = helpers.validate_uprn(uprn)

    if valid_uprn:
        response = requests.post('https://land-property-platform.herokuapp.com/is_it_in_wales', data = {'uprn':'uprn'})
        print(response.text)
        # data = response.json()
        
        # in_wales = data.get('in_wales', None)


    # in_wales = None
    # if uprn == '12345':
    #     in_wales = 'yes'
    # elif uprn == '54321':
    #     in_wales = 'partial'
    # elif uprn == '78910':
    #     in_wales = 'not found'
    # elif uprn == '10987':
    #     in_wales = 'no'

    if in_wales == None:
        raise Exception("Unhandled exception")

    return render_template('result.html', uprn=uprn, valid_uprn=valid_uprn, in_wales=in_wales)

