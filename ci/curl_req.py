import requests
from requests.auth import HTTPBasicAuth
import base64


user = 's-teamcity-iam'
password = ''
param_name = 'aws_secret_access_key'
param_value = 'test2'
param_type = 'password'


url = 'http://teamcity.seloger.com/httpAuth/app/rest/projects/Exploit_Fs01homeUser/parameters/'+param_name
payload = '<property name="%s" value="%s"><type rawValue="%s"/></property>' % (param_name, param_value, param_type)
headers = {'content-type': 'application/xml', 'Origin': 'http://teamcity.seloger.com'}

try:
    r = requests.put(url, auth=HTTPBasicAuth(user, password), data=payload, headers=headers)
except Exception:
    pass