#!/usr/bin/env python

import json


mydata = json.load(open('list.json'))

for i in mydata:
    with open('template.txt') as template, open(i["FQDN"]+'.cfg',"w+") as output:
        for line in template:
            for key, value in i.items():
                line = line.replace(key, str(value))
            output.write(line)

          
