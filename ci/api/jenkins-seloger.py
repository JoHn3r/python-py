import boto3
import json
import unittest
import requests
import jenkinsapi

# def lambda_handler(event, context):
#     secret_content = sm_secrets()
#     print (secret_content)
#     result=jenkins_curl(secret_content)
#     if not analyze_queue(result):
#         print ('The queue is empty')
#     else:
#         print (analyze_queue(result))
#     return {
#         'statusCode': 200,
#         'body': json.dumps(analyze_queue(result))
#     }

class JenkinsSelogerApi:

    def __init__(self, url):
        # https:///queue/api/json?pretty=true
        self.url = url

    # def get_server_instance(self):
    #     #jenkins_url = 'https://'
    #     server = Jenkins(self.url, username='', password='')
    #     return server
            
    # def jenkins_curl(self, j):
    #     user = j['username']
    #     password = j['password']
    #     try:
    #         r = requests.get(self.url, auth=(user, password))
    #         return r
    #     except:
    #         print ('Unable to retrieve the username/password')
        
    # def analyze_queue(self, r):
    #     analyz = json.loads(r.text)
    #     return analyz['items']
