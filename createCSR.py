#!/usr/bin/env python

import json


mydata = json.load(open('list.json'))

for i in mydata:
    with open('template.txt') as template, open(i["FQDN"]+'.cfg',"w+") as output:
        for line in template:
            for key, value in i.items():
                if key == "ALT_NAMES":
                    l = []
                    for v in value:
                        l.append("DNS:" + v)
                        final_list = ",".join(l)
                    line = line.replace(key, final_list)
                else:
                    line = line.replace(key, value)
            output.write(line)

          
