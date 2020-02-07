import boto3
import json


class JenkinsApi:
    """ Class pour monitorer Jenkins via API"""
    def __init__(self):
        pass

    def sm_secrets(self, secret_name):
        # secret_name = 'shared-services/jenkins/admin'
        client = boto3.client('secretsmanager')
        try:
            secret = client.get_secret_value(SecretId=secret_name)
            j = json.loads(secret["SecretString"])
            return j
        except:
            print('Error retrieving secret') 

    def jenkins_curl(self, json):
        url = ''
        user = j['username']
        password = j['password']
        try:
            r = requests.get(url, auth=(user, password))
            return r
        except:
            print('Unable to retrieve the username/password')

    def analyze_queue(self, json):
        analyz = json.loads(r.text)
        return analyz['items']
