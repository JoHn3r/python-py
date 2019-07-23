#!/usr/bin/env python3

import boto3
import json

def getExport():
    client = boto3.client('cloudformation')
    export_list=client.list_exports()
    return export_list

def prettyJson(list):
    return json.dumps(list, indent=2)



def parameterValue(json_parameters,occ):
    name_value=json_parameters["Exports"][occ]["Name"]
    value=json_parameters["Exports"][occ]["Value"]
    return print(name_value + " = " + value)

if __name__ == '__main__':
    exports=getExport()
    for i in range(1,100):
        parameterValue(exports,i)
