from flask import Flask, render_template, request, redirect
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/api_call', methods=['POST'])
def api_call(req_body):

    api_url = 'https://8nofgv3pg0.execute-api.us-east-2.amazonaws.com/default/EC2Scheduler'

    req_body = json.dumps(req_body)
    req = requests.post(api_url, data = req_body)
    decoded_data = req.content.decode("utf-8") 
    return decoded_data




if __name__ == "__main__":
    app.run(debug=True)