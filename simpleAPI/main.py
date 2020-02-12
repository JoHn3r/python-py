import subprocess
import os
import json
import requests
import dominate
from datetime import datetime
from flask import abort, Flask, request, Response, render_template

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def getInf():
    f= open("./templates/main.htm","w+")
    for i in range(1,6):
        r = requests.get(f'http://search-list-rct-{i}.seloger.com/healthcheck')
        if r.json() == 'OK':
            f.write(f'<BODY><H2 style="color:green;">RCT{i} : OK</H1>\n')
        else:
            f.write(f'<BODY><H2 style="color:red;">RCT{i} : KO</H1>\n')
    now = datetime.now()
    f.write(f'<BODY><H3>{now}</H3>\n<meta http-equiv="refresh" content="30">')
    f.close()
    return render_template('main.htm')

@app.route("/repos", methods = ['GET','POST'])
def repos():
    f= open("./templates/repos.htm","w+")
    for i in range(1,6):
        r = requests.get(f'http://search-list-rct-{i}.seloger.com/healthcheck')
        if r.json() == 'OK':
            f.write(f'<BODY><H2 style="color:green;">RCT{i} : OK</H1>\n')
    f.write('<meta http-equiv="refresh" content="30">')
    f.close()
    return render_template('main.htm')

if __name__ == "__main__":
    app.run()
