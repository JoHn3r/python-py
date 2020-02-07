import boto3
import json

class SecretManager:
    def __init__(self,secret_name):
        self.secret_name = secret_name

    def sm_secrets(self):
            # secret_name = 'shared-services/jenkins/admin'
            client = boto3.client('secretsmanager')
            try:
                secret = client.get_secret_value(SecretId=self.secret_name)
                j = json.loads(secret["SecretString"])
                return j
            except:
                print ('Error retrieving secret')