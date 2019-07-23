import subprocess
import os
import json
from flask import abort
from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def getInf():
    # if not request.json:
    #     abort(400)
    pow_res=subprocess.Popen(['powershell','Get-ChildItem | ?{ $_.PSIsContainer } | Select-Object -exp Name'],stdout=subprocess.PIPE,shell=True)
    js=json.dumps(str(pow_res.communicate()))
    resp=Response(js, status=200, mimetype='application/json')
    return resp
if __name__ == "__main__":
    app.run()
