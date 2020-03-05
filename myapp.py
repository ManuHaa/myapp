#import requests
import psutil
import json
import time
import os




from flask import Flask, render_template, send_from_directory,request
app = Flask(__name__, static_url_path='')
app.debug = True


@app.route('/')
def hello_world():

    cpuLoad = str( psutil.cpu_percent())
    return '<h2>Hello, World!</h2> <h3>my CPU Load is at: '+cpuLoad+'</h3>'



@app.route('/test')
def api_test():
    name = "anyuser"
    if "name" in request.args: 
        name = request.args.get("name")
    company = request.args.get("company")
    return render_template('test.html',name=name,company=company)


@app.route('/index')
def api_index():
    return render_template('index.html')

@app.route('/news')
def api_news():
    return render_template('news.html')

@app.route('/contact')
def api_contact():
    return render_template('contact.html')

@app.route('/about')
def api_about():
    return render_template('about.html')


@app.route('/api/contactform', methods=["POST"] )
def contactform():
    curDir = os.path.dirname(os.path.realpath(__file__))
    curTime = int(time.time())
    kvStore ={}  
    if len(request.form) > 0:
        for key,val in request.form.items():
            kvStore[key] = val

    jsonOut = json.dumps(kvStore)
    f = open(curDir+"/"+ str(curTime)+".txt","w+")
    f.write(jsonOut)
    return jsonOut 





if __name__ == '__main__':
    app.run(host="0.0.0.0")